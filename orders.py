import datetime
from storage import save_orders

#orderplacement
orders = []
def place_order(orders, menu):
    while True:
        customer_name = input("Enter your name: ")
        if customer_name.strip():
            break
    try:
        table_number = int(input("Enter your Table number: "))
    except ValueError:
            print("Please Enter a valid number")
    
    items =[]
    print("\n Enter items and quantity")
    print("Enter 'q' to stop ordering")
    
    while True:
        item = input("Enter item name:").title().strip()

        if item.lower().strip() == 'q':
            print("Order placement completed.")
            break
        
        found = False
        for category in menu:
            if item in menu[category]:
                found = True
                
        if not found:
            print("Item not availabe in menu")
            continue
        while True:
            try:
                quantity = int(input("Enter quantity:"))
                break
            except ValueError:
                print("Quantity must be a number")
        
        items.append(
        {"item": item,
        "quantity": quantity
              })
            
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        pending = "pending"   
    order_id = f"ORD{len(orders)+1:03}"
    order= {
        "order_id":order_id,
        "table_number": table_number,
        "customer_name": customer_name,
        "items":items,
        "status":"pending",
        "timestamp":timestamp
        }
    
    orders.append(order)
    
    print("\n Order placed successfully")
    print(f" Here is your order: \n {order}")



#view_active_orders

def view_active_orders(orders):
    
    for order in orders:
        if order["status"] == "pending":
            print(order)



