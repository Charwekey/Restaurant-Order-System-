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




#mark as served

def mark_as_served(orders):
    
    target_id = input("Please enter your order_id: ")
    
    found = False
    
    for order in orders:
        if order["order_id"] == target_id:
            found = True
            
        
            if order["status"] == "pending":
                order["status"] = "served"
                print("Order Marked as served")
            else:
                print("Order already marked as served")
            break
        
    if not found:
        print("Order not found")
        
            
        
        
        
#cancel_order

def cancel_order(orders):
    
    target_order_id = input("Enter your order id: ")
    
    found = False
    
    for order in orders:
        if order["order_id"] == target_order_id:
            found = True 
            
            if order["status"] != "pending":
                print("Order has already been served. It cannot be cancelled.")
                break
            
            confirm = input("Are you sure you want to cancel this order? (yes/no): ")
            if confirm.lower() == "yes":
                orders.remove(order)
                save_orders(orders)
                
                print("Order cancelled successfully.")
            else:
                print("Cancellation aborted.")

            break
        
    if not found:
       print("Order Id not found")
        