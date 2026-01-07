# order_management.py

import orders_data
from collections import Counter

def show_orders():
    print("\nExisting Orders:")
    for order in orders_data.orders:
        print(f"{order['id']} | {order['name']} | {order['location']} | {order['items']}")

def summary():
    total_items = 0
    item_counter = Counter()

    for order in orders_data.orders:
        for item, qty in order["items"]:
            total_items += qty
            item_counter[item] += qty

    print("\n📊 Summary")
    print("Total Customers:", len(orders_data.orders))
    print("Total Items Ordered:", total_items)
    if item_counter:
        print("Most Ordered Item:", item_counter.most_common(1)[0])

def update_order():
    cid = int(input("Enter Customer ID to update: "))
    for order in orders_data.orders:
        if order["id"] == cid:
            item_name = input("Enter item name to update: ")
            new_qty = int(input("Enter new quantity: "))
            for i in range(len(order["items"])):
                if order["items"][i][0] == item_name:
                    order["items"][i] = (item_name, new_qty)
                    print("✅ Order Updated Successfully!")
                    return
    print("Order Not Found")

def delete_order():
    cid = int(input("Enter Customer ID to delete: "))
    orders_data.orders[:] = [o for o in orders_data.orders if o["id"] != cid]
    print("🗑️ Order Deleted")

while True:
    print("\n🧾 SmartGrocery Dashboard")
    summary()
    show_orders()

    print("""
1. Update Order
2. Delete Order
3. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        update_order()
    elif choice == "2":
        delete_order()
    elif choice == "3":
        break
