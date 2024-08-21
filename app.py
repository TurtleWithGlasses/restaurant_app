from flask import Flask, render_template, request
from menu_data import food_dict, drink_dict, dessert_dict
import json
import subprocess

app = Flask(__name__)

def send_order_to_worker(order):
    # sends the order to the worker
    result = subprocess.run(["python3", "worker.py"], input=json.dumps(order), text=True, capture_output=True)
    print("Raw worker output:", result.stdout.strip())
    
    if result.returncode == 0:
        return json.loads(result.stdout.strip())
    else:
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
    
    # Collect selected items
    for item, price in food_dict.items():
        quantity = int(request.form.get(f"food_{item}", 0))
        if quantity > 0:
            selected_items[item] = quantity
            food_total += quantity * price

    for item, price in drink_dict.items():
        quantity = int(request.form.get(f"drink_{item}", 0))
        if quantity > 0:
            selected_items[item] = quantity
            drink_total += quantity * price

    for item, price in dessert_dict.items():
        quantity = int(request.form.get(f"dessert_{item}", 0))
        if quantity > 0:
            selected_items[item] = quantity
            dessert_total += quantity * price
    
    total = food_total + drink_total + dessert_total
    vat = total *0.18
    total_including_vat = total + vat
    
    # Send the order to worker.py
    worker_response = send_order_to_worker(selected_items)

    return render_template(
        "index.html",
        food_dict=food_dict,
        drink_dict=drink_dict,
        dessert_dict=dessert_dict,
        food_total = food_total,
        drink_total=drink_total,
        dessert_total=dessert_total,
        total_including_vat=total_including_vat,
        selected_items = selected_items,
        preparation_details=worker_response.get("preparation_details", {}),
        worker_response=worker_response["status"]
    )

if __name__ == "__main__":
    app.run(debug=True)
