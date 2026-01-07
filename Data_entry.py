# data_entry.py

import datetime
import orders_data

def show_items():
    print("\nAvailable Items:")
    for i, item in enumerate(orders_data.items_catalog.keys(), start=1):
        print(f"{i}. {item.title()}")

def take_order():
    show_items()

    items = input("\nEnter item names (comma separated): ").lower().split(",")
    quantities = input("Enter respective quantities (comma separated): ").split(",")

    selected_items = []
    for i in range(len(items)):
        selected_items.append((items[i].strip(), int(quantities[i])))

    print("\nYour Selected Items:")
    print(selected_items)

    confirm = input("\nType 'confirmed' to proceed with your order: ").lower()
    if confirm != "confirmed":
        print("Order Cancelled!")
        return

    name = input("Name: ")
    location = input("Location: ")
    comments = input("Special Comments: ")

    orders_data.customer_id_counter += 1
    customer_id = orders_data.customer_id_counter

    order = {
        "id": customer_id,
        "name": name,
        "location": location,
        "items": selected_items,
        "comments": comments,
        "time": datetime.datetime.now()
    }

    orders_data.orders.append(order)

    print("\n✅ Order Confirmed Successfully!")
    print("Customer ID:", customer_id)
    print("Customer:", name)
    print("Location:", location)
    print("Items Ordered:", selected_items)
    print("Time:", order["time"])

while True:
    print("\n🛒 Welcome to SmartGrocery")
    take_order()
    again = input("\nNew Customer? (yes/no): ").lower()
    if again != "yes":
        break
