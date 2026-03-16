from menu import menu, display_menu
from orders import place_order, view_active_orders, mark_as_served, cancel_order
from billing import generate_order_bill
from storage import load_orders, save_orders




orders = load_orders()

while True:

    print("\n Welcome to SYNTAX BISTRO")
    print("1. Display Menu")
    print("2. Place Order")
    print("3. View Active Orders")
    print("4. Mark Order as Served")
    print("5. Generate Bill")
    print("6. Cancel Order")
    print("7. Exit")

    try:
        choice = int(input("Choose an option: "))

        if choice == 1:
            display_menu(menu)

        elif choice == 2:
            place_order(orders, menu)
            save_orders(orders)

        elif choice == 3:
            view_active_orders(orders)

        elif choice == 4:
            mark_as_served(orders)

        elif choice == 5:
            generate_order_bill(orders, menu)

        elif choice == 6:
            cancel_order(orders)

        elif choice == 7:
            save_orders(orders)
            print("System closed. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 7.")

    except ValueError:
        print("Invalid input. Please enter a number.")