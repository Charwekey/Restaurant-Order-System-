def generate_order_bill(orders, menu):

    while True:
        try:
            target_table_number = int(input("Kindly enter your table number to generate order bill: ").strip())
            break
        except ValueError:
            print("Table number must be a number. Please try again.")

    sub_total = 0
    table_has_order = False
    served_order_found = False

    for order in orders:

        if order["table_number"] == target_table_number:
            table_has_order = True

            if order["status"] == "pending":
                print("Your order is still pending. Please check back later.")
                return

            if order["status"] == "served":
                served_order_found = True

                print("\n------ RECEIPT ------")
                print(f"Table: {target_table_number}")
                print(f"Order ID: {order['order_id']}")
                print(f"Customer Name: {order['customer_name']}")
                print(f"Timestamp: {order['timestamp']}")
                print("----------------------\n")

                print("Items Ordered:\n")

                for item in order["items"]:
                    item_name = item["item"]
                    quantity = item["quantity"]

                    for category in menu:
                        if item_name in menu[category]:
                            price = menu[category][item_name]

                            item_total = price * quantity
                            sub_total += item_total

                            print(f"{item_name}")
                            print(f"Price: GHC {price} each")
                            print(f"Quantity: {quantity}")
                            print(f"Item Total: GHC {item_total}\n")

    if not table_has_order:
        print(f"No orders found for table number {target_table_number}")
        return

    if not served_order_found:
        return

    vat = sub_total * 0.15
    grand_total = sub_total + vat

    print("----------------------")
    print(f"Subtotal: GHC {sub_total}")
    print(f"VAT (15%): GHC {vat}")
    print(f"Grand Total: GHC {grand_total}")
    print("----------------------")