import tkinter as tk
from menu_section import MenuSection, setup_order_buttons, order_number_label, food_dict, drink_dict, dessert_dict


window = tk.Tk()
window.geometry("1200x950")
window.title("Restaurant Order App")

# Create frames for each section
food_section = MenuSection(window, food_dict, "Foods", row=1, column=0)
drink_section = MenuSection(window, drink_dict, "Drinks", row=1, column=1)
dessert_section = MenuSection(window, dessert_dict, "Desserts", row=1, column=2)

setup_order_buttons(window, food_section, drink_section, dessert_section)
order_number_label(window)

window.mainloop()
