from flask import Flask, render_template, request
from menu_data import food_dict, drink_dict, dessert_dict
import json
import subprocess

app = Flask(__name__)

def send_order_to_worker(order):
    # sends the order to the worker
    result = subprocess.run(["python3", "worker.py"], input=json.dumps(order), text=True, capture_output=True)
    
    if result.returncode != 0:
        return "Error in worker process"
    
    return result.stdout.strip()

@app.route("/")
def index():
    return render_template("index.html", food_dict=food_dict, drink_dict=drink_dict, dessert_dict=dessert_dict)

@app.route("/calculate", methods=["POST"])
def calculate():
    # gets the sum of selected products on the menu and calculates the price & amount
    food_total = sum(int(request.form.get(f"food_{item}", 0)) * price for item, price in food_dict.items())
    drink_total = sum(int(request.form.get(f"drink_{item}", 0)) * price for item, price in drink_dict.items())
    dessert_total = sum(int(request.form.get(f"dessert_{item}", 0)) * price for item, price in dessert_dict.items())

    total = food_total + drink_total + dessert_total
    vat = total * 0.18
    total_including_vat = total + vat

    # order is gathered in a dictionary to be sent to the worker
    order = {}
    for item in food_dict.keys():
        quantity = int(request.form.get(f"food_{item}"), 0)
        if quantity > 0:
            order[item] = quantity
    for item in drink_dict.keys():
        quantity = int(request.form.get(f"drink_{item}"), 0)
        if quantity > 0:
            order[item] = quantity
    for item in dessert_dict.keys():
        quantity = int(request.form.get(f"dessert_{item}"), 0)
        if quantity > 0:
            order[item] = quantity
    
    worker_response = send_order_to_worker(order)

    return render_template(
        "index.html",
        food_dict=food_dict,
        drink_dict=drink_dict,
        dessert_dict=dessert_dict,
        food_total=food_total,
        drink_total=drink_total,
        dessert_total=dessert_total,
        total_including_vat=total_including_vat,
        worker_response=worker_response
    )

if __name__ == "__main__":
    app.run(debug=True)
