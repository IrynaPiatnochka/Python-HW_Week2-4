
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Adding new category of "Baverages" to the menu

restaurant_menu["Beverages"] = "Coffee", "Tea"
print(restaurant_menu)

# Updating the price of the item in the menu

restaurant_menu["Main Course"]["Steak"] = "17.99"
print(restaurant_menu)

# #Remove "Bruschetta" from "Starters"

del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)
