import ast
#save_orders

def save_orders(orders):

    with open("orders.txt", "w") as file:
        for order in orders:
            file.write(str(order) + "\n")


#load_orders
def load_orders():

    orders = []

    try:
        with open("orders.txt", "r") as file:
            for line in file:
                orders.append(ast.literal_eval(line.strip()))

    except FileNotFoundError:
        pass

    return orders