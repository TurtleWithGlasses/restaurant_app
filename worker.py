import sys
import json
import time

# Preparation interval for each product
preparation_times = {
    "Hamburger": 10, "Cheeseburger": 8, "Steak": 15, "Pizza": 12,
    "Tuna Sandwich": 7, "Cheese Sandwich": 5, "Tuna Salad": 6,
    "Fish Salad": 9, "Pasta": 10, "Water": 2, "Coke": 2,
    "Orange Juice": 3, "Coffee": 5, "Beer": 2, "Wine": 4,
    "Sprite": 2, "Whiskey": 4, "Dr Pepper": 2, "Apple Pie": 6,
    "Cheesecake": 8, "Brownie": 7, "Banana Bread": 10,
    "Milkshake": 5, "Baklava": 12, "Orange Cake": 8,
    "Fresh Fruits": 5, "Doughnuts": 9
}

# Worker remains idle
worker_busy = False

def process_order(order):
    global worker_busy

    if worker_busy:
        print("Worker is busy")
        return {"status":"BUSY"}
    
    worker_busy = True
    preparation_details = {}

    # Process each item in the order
    for item, quantity in order.items():
        if item in preparation_times:
            item_time = preparation_times[item] * quantity
            time.sleep(item_time)  # Simulate the preparation time
            preparation_details[item] = "READY"  # Update status to READY

    worker_busy = False
    return {"status": "Order Ready", "preparation_details": preparation_details}

if __name__ == "__main__":
    order_data = sys.stdin.read()
    try:        
        order = json.loads(order_data)
        result = process_order(order)
        print(json.dumps(result))
    except json.JSONDecodeError as e:
        print(json.dumps({"status": "Error", "message": str(e)}))
