import csv
import tkinter as tk
from datetime import datetime

class MenuSection:
    def __init__(self, master, items, title, row, column):
        self.master = master
        self.items = items
        self.title = title
        self.row = row
        self.column = column
        self.buttons = []
        self.create_section()

    def create_section(self):
        frame = tk.Frame(self.master)
        frame.grid(row=self.row, column=self.column, padx=10, pady=10)

        section_label = tk.Label(frame, text=self.title, font=("Arial", 15))
        section_label.grid(row=0, column=1)

        for number, (item_name, item_price) in enumerate(self.items.items(), start=1):
            button = self.create_item_button(frame, number, item_name, item_price)
            self.buttons.append(button)

    def create_item_button(self, frame, number, item_name, item_price):
        button = {}
        button['name'] = item_name
        button['price'] = item_price
        button['value'] = 0

        item_label = tk.Label(frame, text=f"{item_name} (${item_price})", font=("Arial", 12))
        item_label.grid(row=number, column=0, padx=5, sticky="w")

        decrease_button = tk.Button(frame, text="-", command=lambda: self.decrease_number(button), width=5)
        decrease_button.grid(row=number, column=1, padx=5, sticky="w")

        increase_button = tk.Button(frame, text="+", command=lambda: self.increase_number(button), width=5)
        increase_button.grid(row=number, column=2, padx=5, sticky="w")

        value_label = tk.Label(frame, text=str(button['value']), width=5, font=("Arial", 24))
        value_label.grid(row=number, column=3, padx=5)

        button['label'] = value_label
        return button

    def decrease_number(self, button):
        if button['value'] > 0:
            button['value'] -= 1
            button['label'].config(text=str(button['value']))

    def increase_number(self, button):
        button['value'] += 1
        button['label'].config(text=str(button['value']))

    def get_total(self):
        return sum(button['value'] * button['price'] for button in self.buttons)
    
    def reset(self):
        """Reset all the quantities in the section to zero."""
        for button in self.buttons:
            button['value'] = 0
            button['label'].config(text=str(button['value']))

# Order management functionality
order_number = 1

def setup_order_buttons(window, food_section, drink_section, dessert_section):
    global food_label, drinks_label, desserts_label, total_label

    food_label = tk.Label(window, text="Foods: $0.00", font=("Arial", 16))
    food_label.grid(row=10, column=0, columnspan=3, pady=20)

    drinks_label = tk.Label(window, text="Drinks: $0.00", font=("Arial", 16))
    drinks_label.grid(row=11, column=0, columnspan=3, pady=20)

    desserts_label = tk.Label(window, text="Desserts: $0.00", font=("Arial", 16))
    desserts_label.grid(row=12, column=0, columnspan=3, pady=20)

    total_label = tk.Label(window, text="Total (incl. VAT): $0.00", font=("Arial", 16))
    total_label.grid(row=13, column=0, columnspan=3, pady=20)

    calculate_and_save_button = tk.Button(window, text="Calculate & Save Order", command=lambda: calculate_and_save_order(food_section, drink_section, dessert_section), font=("Arial", 16))
    calculate_and_save_button.grid(row=3, column=0, columnspan=3, pady=10)

def calculate_and_save_order(food_section, drink_section, dessert_section):
    global order_number

    order_number_str = f"{order_number:04d}"
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Being Prepared"

    # Calculate totals
    food_total = food_section.get_total()
    drink_total = drink_section.get_total()
    dessert_total = dessert_section.get_total()

    total = food_total + drink_total + dessert_total
    vat = total * 0.18
    total_including_vat = total + vat

    food_label.config(text=f"Foods: ${food_total:.2f}")
    drinks_label.config(text=f"Drinks: ${drink_total:.2f}")
    desserts_label.config(text=f"Desserts: ${dessert_total:.2f}")
    total_label.config(text=f"Total (incl. VAT): ${total_including_vat:.2f}")

    save_order_to_csv(order_number_str, current_datetime, status, food_section, drink_section, dessert_section)

    # Reset order
    food_section.reset()
    drink_section.reset()
    dessert_section.reset()

    order_number += 1
    order_label.config(text=f"Order #{order_number:04d}")

def save_order_to_csv(order_number_str, current_datetime, status, food_section, drink_section, dessert_section):
    with open("orders.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Order Number", "Date & Time", "Item", "Quantity", "Price", "Status"])

        for button in food_section.buttons:
            if button['value'] > 0:
                writer.writerow([order_number_str, current_datetime, button['name'], button['value'], button['price'], status])

        for button in drink_section.buttons:
            if button['value'] > 0:
                writer.writerow([order_number_str, current_datetime, button['name'], button['value'], button['price'], status])

        for button in dessert_section.buttons:
            if button['value'] > 0:
                writer.writerow([order_number_str, current_datetime, button['name'], button['value'], button['price'], status])

def order_number_label(window):
    global order_label
    order_label = tk.Label(window, text=f"Order #{order_number:04d}", font=("Arial", 16))
    order_label.grid(row=5, column=0, columnspan=3, pady=10)

food_dict = {
    "Hamburger": 15, "Cheeseburger": 10, "Steak": 20, "Pizza": 12, 
    "Tuna Sandwich": 10, "Cheese Sandwich": 7, "Tuna Salad": 8, 
    "Fish Salad": 10, "Pasta": 12
}

drink_dict = {
    "Water": 2, "Coke": 5, "Orange Juice": 3, "Coffee": 7, 
    "Beer": 5, "Wine": 12, "Sprite": 5, "Whiskey": 15, "Dr Pepper": 10
}

dessert_dict = {
    "Apple Pie": 5, "Cheesecake": 4, "Brownie": 5, "Banana Bread": 7, 
    "Milkshake": 5, "Baklava": 10, "Orange Cake": 5, "Fresh Fruits": 7, 
    "Doughnuts": 8
}