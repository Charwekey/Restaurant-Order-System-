#dictionary of menu display
import datetime
import ast
menu = {
    "Starters": {
        "Garlic Bread": 5,
        "Spring Rolls":  6,
        "Chicken Wings": 8
    },
    "Mains": {
        "Burger":  12,
        "Pizza":  15,
        "Grilled Chicken": 14
    },
    "Drinks": {
        "Coke":3,
        "Orange Juice":  4,
        "Water": 2
    },
    "Desserts": {
        "Ice Cream": 5,
        "Chocolate Cake": 6,
        "Fruit Salad": 4
    }
}


def display_menu(menu):
    print(f" \n Restaurant Menu" )
    
    for category, items in menu.items():
        print(f"\n {category}")
        
        for item, price in items.items():
            print(f" \n {item}: GHC {price}")
        

