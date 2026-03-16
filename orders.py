import datetime
from storage import save_orders

# order placement
orders = []

def place_order(orders, menu):

    # CUSTOMER NAME
    while True:
        customer_name = input("Enter your name: ").strip()

        if customer_name == "":
            print("Kindly enter your name.")
        else:
            break

    # TABLE NUMBER
    while True:
        table_input = input("Enter your Table number: ").strip()

        if table_input == "":
            print("Kindly enter your table number.")
            continue

        try:
            table_number = int(table_input)
            break
        except ValueError:
            print("Please enter a digit number.")

    items = []

    print("\nEnter items and quantity")
    print("Enter 'q' to stop ordering")

    while True:

        item = input("Enter item name: ").strip()

        if item == "":
            print("Please enter an item name.")
            continue

        if item.lower() == 'q':
            if len(items) == 0:
                print("You must order at least one item.")
                continue
            print("Order placement completed.")
            break

        item = item.title()

        # CHECK IF ITEM EXISTS IN MENU
        found = False
        for category in menu:
            if item in menu[category]:
                found = True
                break

        if not found:
            print("Item not available in menu.")
            continue

        # QUANTITY
        while True:
            quantity_input = input("Enter quantity: ").strip()

            if quantity_input == "":
                print("Please enter quantity.")
                continue

            try:
                quantity = int(quantity_input)

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

                break
            except ValueError:
                print("Quantity must be a number.")

        items.append({
            "item": item,
            "quantity": quantity
        })

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    order_id = f"ORD{len(orders)+1:03}"

    order = {
        "order_id": order_id,
        "table_number": table_number,
        "customer_name": customer_name,
        "items": items,
        "status": "pending",
        "timestamp": timestamp
    }

    orders.append(order)

    print("\nOrder placed successfully")
    print(f"Here is your order:\n{order}")


# VIEW ACTIVE ORDERS
def view_active_orders(orders):

    found = False

    for order in orders:
        if order["status"] == "pending":
            print(order)
            found = True

    if not found:
        print("No active orders.")


# MARK AS SERVED
def mark_as_served(orders):

    while True:
        target_id = input("Please enter your order_id: ").strip()

        if target_id == "":
            print("Please enter an order ID.")
        else:
            break

    found = False

    for order in orders:

        if order["order_id"] == target_id:
            found = True

            if order["status"] == "pending":
                order["status"] = "served"
                print("Order marked as served.")
            else:
                print("Order already marked as served.")

            break

    if not found:
        print("Order not found.")


# CANCEL ORDER
def cancel_order(orders):

    while True:
        target_order_id = input("Enter your order id: ").strip()

        if target_order_id == "":
            print("Please enter an order ID.")
        else:
            break

    found = False

    for order in orders:

        if order["order_id"] == target_order_id:
            found = True

            if order["status"] != "pending":
                print("Order has already been served. It cannot be cancelled.")
                break

            while True:
                confirm = input("Are you sure you want to cancel this order? (yes/no): ").strip().lower()

                if confirm == "":
                    print("Please type yes or no.")
                    continue

                if confirm == "yes":
                    orders.remove(order)
                    save_orders(orders)
                    print("Order cancelled successfully.")
                    break

                elif confirm == "no":
                    print("Cancellation aborted.")
                    break

                else:
                    print("Please type 'yes' or 'no'.")

            break

    if not found:
        print("Order ID not found.")