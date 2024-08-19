import sys
import json
import time

# preparation interval for each product
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

# worker remains idle
worker_busy = False

def process_order(order):
    global worker_busy

    if worker_busy:
        print("Worker is busy")
        return "BUSY"
    
    worker_busy = True
    print(f"Processing order: {order}")

    total_time = 0

    # getting the total item and quantity that was received with the order
    for item, quantity in order.items():
        if item in preparation_times:
            item_time = preparation_times[item] * quantity
            print(f"Preparing item {item}: {item_time} seconds")
            time.sleep(item_time)
            total_time += item_time

    # when the order is processed, worker goes back to idle
    print("Order is ready!")
    worker_busy = False
    return "Order Ready"

if __name__ == "__main__":
    order_data = sys.stdin.read()
    order = json.loads(order_data)
    result = process_order(order)
    print(result)