from flask import Flask, render_template, request
from menu_data import food_dict, drink_dict, dessert_dict
from models import db, Order, OrderItem
import json
import subprocess
import time
from datetime import datetime

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

def send_order_to_worker(order):
    # Sends the order to the worker
    result = subprocess.run(["python3", "worker.py"], input=json.dumps(order), text=True, capture_output=True)
    print("Raw worker output:", result.stdout.strip())
    
    if result.returncode == 0:
        return json.loads(result.stdout.strip())
    else:
        print("Worker error output:", result.stderr.strip())
        return {"status": "Error", "preparation_details": {}}

@app.route("/")
def index():
    print("Food Dictionary:", food_dict)
    print("Drink Dictionary:", drink_dict)
    print("Dessert Dictionary:", dessert_dict)
    return render_template("index.html", food_dict=food_dict, drink_dict=drink_dict, dessert_dict=dessert_dict)

@app.route("/calculate", methods=["POST"])
def calculate():
    selected_items = {}

    food_total = 0
    drink_total = 0
    dessert_total = 0

    # Collect selected items and calculate totals
    for item, price in food_dict.items():
        quantity = int(request.form.get(f"food_{item}", 0))
        if quantity > 0:
            selected_items[item] = quantity
            food_total += price * quantity

    for item, price in drink_dict.items():
        quantity = int(request.form.get(f"drink_{item}", 0))
        if quantity > 0:
            selected_items[item] = quantity
            drink_total += price * quantity

    for item, price in dessert_dict.items():
        quantity = int(request.form.get(f"dessert_{item}", 0))
        if quantity > 0:
            selected_items[item] = quantity
            dessert_total += price * quantity

    total = food_total + drink_total + dessert_total
    vat = total * 0.18
    total_including_vat = total + vat

    # Generate unique order number
    order_number = f"ORD-{int(time.time())}"

    # Save order & items to the database
    order = Order(
        order_number=order_number,
        date=datetime.now().strftime("%Y-%m-%d"),
        time=datetime.now().strftime("%H:%M:%S"),
        total=total,
        vat=vat,
        total_including_vat=total_including_vat
    )
    db.session.add(order)
    db.session.flush()  # Ensure order.id is available for the order items

    for item, quantity in selected_items.items():
        item_price = (food_dict.get(item) or drink_dict.get(item) or dessert_dict.get(item))
        order_item = OrderItem(
            order_id=order.id,
            item_name=item,
            quantity=quantity,
            price=item_price * quantity
        )
        db.session.add(order_item)
    
    db.session.commit()

    # Send the order to worker.py
    worker_response = send_order_to_worker(selected_items)

    # handle worker response
    if worker_response["status"] == "Order Ready":
        print("Order is ready, generating receipt...")
        # generate the receipt details
        receipt = {
            "order_number": order_number,
            "date": order.date,
            "time": order.time,
            "order_items": [
                {"name": item.item_name, "quantitiy": item.quantitiy, "price": item.price} for item in order.items
            ],
            "total": total,
            "vat": vat,
            "total_including_vat": total_including_vat
        }
        print("Receipt data:", receipt)
    else:
        print("Worker did not complete the order, response:", worker_response)

    # Generate the receipt details
    receipt = {
        "order_number": order_number,
        "date": order.date,
        "time": order.time,
        "order_items": [
            {"name": item.item_name, "quantity": item.quantity, "price": item.price} for item in order.items
        ],
        "total": total,
        "vat": vat,
        "total_including_vat": total_including_vat
    }
    print("Receipt items:", receipt['order_items'])

    return render_template(
        "index.html",
        food_dict=food_dict,
        drink_dict=drink_dict,
        dessert_dict=dessert_dict,
        food_total=food_total,
        drink_total=drink_total,
        dessert_total=dessert_total,
        total_including_vat=total_including_vat,
        selected_items=selected_items,
        preparation_details=worker_response.get("preparation_details", {}),
        worker_response=worker_response["status"],
        receipt=receipt if worker_response["status"] == "Order Ready" else None
    )

if __name__ == "__main__":
    app.run(debug=True)
