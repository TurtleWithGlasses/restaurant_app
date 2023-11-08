import tkinter as tk

window = tk.Tk()
window.geometry("1200x950")
window.title("Restaurant Order App")

welcome_frame = tk.Frame(window)
welcome_frame.grid(row=0, column=0, columnspan=3, sticky="ew")

welcome_label = tk.Label(welcome_frame, text="Welcome", font=("Arial", 24))
welcome_label.pack(padx=10, pady=10)

food_frame = tk.Frame(window)
food_frame.grid(row=1, column=0, padx=10, pady=10)

food_label = tk.Label(food_frame, text="Foods", font=("Arial", 15))
food_label.grid(row=0, column=1)

drink_frame = tk.Frame(window)
drink_frame.grid(row=1, column=1, padx=10, pady=10)

drinks_label = tk.Label(drink_frame, text="Drinks", font=("Arial", 15))
drinks_label.grid(row=0, column=1)

dessert_frame = tk.Frame(window)
dessert_frame.grid(row=1, column=2, padx=10, pady=10)

desserts_label = tk.Label(dessert_frame, text="Desserts", font=("Arial", 15))
desserts_label.grid(row=0, column=1)

food_dict = {"Hamburger": 15, "Cheeseburger": 10, "Steak": 20, "Pizza": 12, "Tuna Sandwich": 10, "Cheese Sandwich": 7, "Tuna Salad": 8, "Fish Salad": 10, "Pasta": 12}
drink_dict = {"Water": 2, "Coke": 5, "Orange Juice": 3, "Coffee": 7, "Beer": 5, "Wine": 12, "Sprite": 5, "Whiskey": 15, "Dr Pepper": 10}
dessert_dict = {"Apple Pie": 5, "Cheesecake": 4, "Brownie": 5, "Banana Bread": 7, "Milkshake": 5, "Baklava": 10, "Orange Cake": 5, "Fresh Fruits": 7, "Doughnuts": 8}

class ButtonForFood:
    def __init__(self, master, number):
        self.number = number
        self.value = 0

        self.food_name = list(food_dict.keys())[number - 1]
        self.food_price = food_dict[self.food_name]

        self.frame = tk.Frame(master)
        self.frame.grid(row=number, column=1, padx=10, sticky="e")

        self.food_label = tk.Label(self.frame, text=f"{self.food_name} (${self.food_price})", font=("Arial", 12))
        self.food_label.grid(row=0, column=0, padx=5, sticky="w")

        self.decrease_button = tk.Button(self.frame, text="-", command=self.decrease_number, width=5)
        self.decrease_button.grid(row=0, column=1, padx=5, sticky="w")

        self.increase_button = tk.Button(self.frame, text="+", command=self.increase_number, width=5)
        self.increase_button.grid(row=0, column=2, padx=5, sticky="w")

        self.label = tk.Label(self.frame, text=str(self.value), width=5, font=("Arial", 24))
        self.label.grid(row=0, column=3, padx=5)

    def decrease_number(self):
        if self.value > 0:
            self.value -= 1
            self.label.config(text=str(self.value))

    def increase_number(self):
        self.value += 1
        self.label.config(text=str(self.value))

class ButtonForDrinks:
    def __init__(self, master, number):
        self.number = number
        self.value = 0

        self.drink_name = list(drink_dict.keys())[number - 1]
        self.drink_price = drink_dict[self.drink_name]

        self.frame = tk.Frame(master)
        self.frame.grid(row=number, column=1, padx=10, sticky="e")

        self.drink_label = tk.Label(self.frame, text=f"{self.drink_name} (${self.drink_price})", font=("Arial", 12))
        self.drink_label.grid(row=0, column=0, padx=5, sticky="w")

        self.decrease_button = tk.Button(self.frame, text="-", command=self.decrease_number, width=5)
        self.decrease_button.grid(row=0, column=1, padx=5, sticky="w")

        self.increase_button = tk.Button(self.frame, text="+", command=self.increase_number, width=5)
        self.increase_button.grid(row=0, column=2, padx=5, sticky="w")

        self.label = tk.Label(self.frame, text=str(self.value), width=5, font=("Arial", 24))
        self.label.grid(row=0, column=3, padx=5)

    def decrease_number(self):
        if self.value > 0:
            self.value -= 1
            self.label.config(text=str(self.value))

    def increase_number(self):
        self.value += 1
        self.label.config(text=str(self.value))

class ButtonForDesserts:
    def __init__(self, master, number):
        self.number = number
        self.value = 0

        self.dessert_name = list(dessert_dict.keys())[number - 1]
        self.dessert_price = dessert_dict[self.dessert_name]

        self.frame = tk.Frame(master)
        self.frame.grid(row=number, column=1, padx=10, sticky="e")

        self.dessert_label = tk.Label(self.frame, text=f"{self.dessert_name} (${self.dessert_price})", font=("Arial", 12))
        self.dessert_label.grid(row=0, column=0, padx=5, sticky="w")

        self.decrease_button = tk.Button(self.frame, text="-", command=self.decrease_number, width=5)
        self.decrease_button.grid(row=0, column=1, padx=5, sticky="w")

        self.increase_button = tk.Button(self.frame, text="+", command=self.increase_number, width=5)
        self.increase_button.grid(row=0, column=2, padx=5, sticky="w")

        self.label = tk.Label(self.frame, text=str(self.value), width=5, font=("Arial", 24))
        self.label.grid(row=0, column=3, padx=5)

    def decrease_number(self):
        if self.value > 0:
            self.value -= 1
            self.label.config(text=str(self.value))

    def increase_number(self):
        self.value += 1
        self.label.config(text=str(self.value))

food_buttons = [ButtonForFood(food_frame, number) for number in range(1, 10)]
drink_buttons = [ButtonForDrinks(drink_frame, number) for number in range(1, 10)]
dessert_buttons = [ButtonForDesserts(dessert_frame, number) for number in range(1, 10)]


food_label = tk.Label(window, text="Foods (incl. VAT): $0.00", font=("Arial", 16))
food_label.grid(row=10, column=0, columnspan=3, pady=20)
drinks_label = tk.Label(window, text="Drinks (incl. VAT): $0.00", font=("Arial", 16))
drinks_label.grid(row=11, column=0, columnspan=3, pady=20)
desserts_label = tk.Label(window, text="Desserts (incl. VAT): $0.00", font=("Arial", 16))
desserts_label.grid(row=12, column=0, columnspan=3, pady=20)
total_label = tk.Label(window, text="Total (incl. VAT): $0.00", font=("Arial", 16))
total_label.grid(row=13, column=0, columnspan=3, pady=20)

# Function to calculate the total including VAT
def calculate_total():
    food_total = sum(button.value * food_dict[button.food_name] for button in food_buttons)
    drink_total = sum(button.value * drink_dict[button.drink_name] for button in drink_buttons)
    dessert_total = sum(button.value * dessert_dict[button.dessert_name] for button in dessert_buttons)

    total = food_total + drink_total + dessert_total
    vat = total * 0.18
    total_including_vat = total + vat

    food_label.config(text=f"Foods (incl. VAT): ${food_total:.2f}")
    drinks_label.config(text=f"Drinks (incl. VAT): ${drink_total:.2f}")
    desserts_label.config(text=f"Desserts (incl. VAT): ${dessert_total:.2f}")
    total_label.config(text=f"Total (incl. VAT): ${total_including_vat:.2f}")

# Create a Calculate Total button
calculate_button = tk.Button(window, text="Calculate Total", command=calculate_total, font=("Arial", 16))
calculate_button.grid(row=3, column=0, columnspan=3, pady=10)


window.mainloop()