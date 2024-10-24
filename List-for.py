import json

def save_inventory(inventory, filename="inventory.json"):
    with open(filename, 'w') as f:
        json.dump(inventory, f)

def load_inventory(filename="inventory.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return [] # an empty list if file does'nt exist.


print("welcome to a program where you save inventory")

Inventory = ["Cake", "Cookie", "Saw"]
Inventory_limit = 4

Inventory = load_inventory()

run = True
while run:
    print("------------------")
    choice = input("What do you want? \n[1] List \n[2] Add a item \n[3] Remove item \n[4] Clear inventory \n[5] Stop \n Input: ")
    if choice == "1":
        print(f"You have {len(Inventory)} items in your inventory:")
        for items in Inventory:
            print(items)
        
    elif choice == "2":
        new_item = input("Input a new item: ")
        if len(Inventory) < Inventory_limit:
            Inventory.append(new_item)
            print(f"{new_item} has been added to inventory!")
        else:
            print("Inventory is full! Cannot add more items.")

    elif choice == "3":
        item_to_remove = input("Remove item: ")
        if item_to_remove in Inventory:
            Inventory.remove(item_to_remove)
            print(f"{item_to_remove} has been removed from inventory.")
        else:
            print(f"{item_to_remove} not found in inventory.")
        
    elif choice == "4":
        print("Inventory has been cleared")
        Inventory.clear()

    elif choice == "5":
        save_inventory(Inventory)
        run = False

    else: 
        print("Invalid choice. Please try again.")


