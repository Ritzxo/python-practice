inventory = {}

def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
        return
    try:
        inventory[item] = {"price": float(price), "stock": int(stock)}
        print(f"Item '{item}' added successfully.")
    except ValueError:
        print("Error: Price and stock must be numeric.")

def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
        return
    try:
        new_stock = inventory[item]["stock"] + int(quantity)
        if new_stock < 0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]["stock"] = new_stock
            print(f"Stock for '{item}' updated successfully.")
    except ValueError:
        print("Error: Quantity must be an integer.")
def check_availability(item):
    if item not in inventory:
        return("Item not found")
    else:
        stock = inventory[item]["stock"]
        return stock

def sales_report(sales):
    running_total = 0
    for item, quantity in sales.items():
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
            continue
        
        if quantity > inventory[item]["stock"]:
            print(f"Error: Insufficient stock for '{item}'.")
            continue
        
        item_revenue = inventory[item]["price"] * quantity
        running_total += item_revenue
        inventory[item]["stock"] -= quantity
    return(f"Total revenue: ${running_total:.2f}")

add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10} 
print(sales_report(sales)) 
print(inventory)