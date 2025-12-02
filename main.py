import database

#this file is the main file that the user sees and navigates

#main menu for user to navigate
menu = '''\nPlease select one of the following options:
1. Add new item.
2. Delete item.
3. Search for an Item.
4. View all items.
5. Update Stock.
6. View sold out Items.
7. View Latest Delivery Person
8. Update Delivery Person
9. Exit

Your selection: '''
welcome = "Welcome to your Hardware Store Database App!"

#prompts
def prompt_add_new_item(): #adds a new item to the database
    itemName = input("Item Name: ")
    itemCategory = input("Item Category: ")
    itemStock = int(input("# in Stock: "))
    itemManufacturer = input("Item Manufacturer: ")
    try:
        itemCost = float(input("Item Cost: "))
        return itemName, itemCategory, itemCost, itemStock, itemManufacturer, "Success"
    except ValueError:
      print("Bad Price Format!")
    return itemName, itemCategory, itemCost, itemStock, itemManufacturer, "Failed"

def prompt_add_manufacturer(): #adds a new manufacturer and their delivery person if not already in the database
    print("\nManufacturer is currently not in our database. Please answer these questions:\n")
    manufacturer_address = input("Manufacturer address: ")
    delivery_day = input("Manufacturers delivery day: ")
    delivery_person = input("Manufacturers current delivery person: ")
    delivery_phone = input("Delivery's phone number: ")
    return manufacturer_address, delivery_day, delivery_person, delivery_phone

def prompt_delete_item(): #deletes an item from the database based on id
    item_options = database.view_items()
    print_items("Items in Database", item_options)
    id_to_del = input("\nWhat item would you like to delete (id)? ")
    return id_to_del

def prompt_search_item(): #searches for an item either by category or item name
    search_option = int(input("Would you like to search by 1. Category or 2. Item Name?: "))
    if search_option == 1:
        searchedItem = input("\nWhat category would you like to search for?: ")
        return searchedItem, "Category"
    elif search_option == 2:
        searchedItem = input("\nWhat is the name of the item you would like to search for?: ")
        return searchedItem, "ItemName"
    else:
        print("Invalid Selection!")
    return None, "Invalid"

def prompt_select_item_for_delivery(): #selects an item to see delivery person based off item id
    item_options = database.view_items()
    print_items("Items in Database", item_options)
    item_id = input("\nSelect an item to see its delivery person (id): ")
    return item_id

def prompt_update_stock():#updates the number of stock for an item based off item id
    item_options = database.view_items()
    print_items("Items in Database", item_options)
    chosenItem = int(input("\nWhich item would you like to update?(id): "))
    newStock = int(input("What is the new # of stock?: "))
    return chosenItem, newStock

def prompt_update_delivery_person(): #updates a delivery person and info for a manufacturer
    manufacturer_options = database.view_manufacturers()
    print_manufacturer_with_delivery(manufacturer_options)
    chosen_manufacturer = input("\nUpdate delivery person for which manufacturer?: ")
    new_delivery_person = input("\nWhat is the new delivery person's name?: ")
    new_delivery_phone = input("\nWhat is the new delivery's phone number?: ")
    return chosen_manufacturer, new_delivery_person, new_delivery_phone

#prints
def print_items(header, items): #prints out a list of items information
    print(f"------ {header} -------")
    for id, itemName, manufacturerName, category, cost, inStock in items:
        print(f"{id}. ${cost} {itemName} - Category: {category} - Manufacturer: {manufacturerName} - Number in Stock: {inStock}")
    print("------------------------")

def print_sold_out_items(items): #prints out a list of sold out items and the next delivery date
    print(f"------ Sold Out Items -------")
    for id, itemName, delivery_date in items:
        print(f"{id}. {itemName} - Next delivery expected {delivery_date}")
    print("------------------------")

def print_delivery_info(delivery): #prints outs a delivery person and their phone number
    print(f"------ Delivery Information -------")
    for delivery_person, delivery_phone in delivery:
        print(f"Item last delivered by: {delivery_person}\nPhone Number: {delivery_phone}")
    print("------------------------")

def print_manufacturer_with_delivery(manufacturers): #prints out manufacturers and their address and delivery information
    print(f"------ Manufacturer Information -------")
    for manufacturer_name, manufacturer_address, delivery_day, delivery_person in manufacturers:
        print(f"{manufacturer_name} - Address: {manufacturer_address} - Delivery Day: {delivery_day}, Delivery Person: {delivery_person}")
    print("------------------------")

# main < -------------
print(welcome)
database.create_tables()

# <-------- Main, program starts here.
while (user_input := input(menu)) != "9":
    if user_input == "1":
        #this adds the item to the database, and depending on if the
        #if the manufacturer exist, it gets the correct information
       itemName, itemCategory, itemCost, inStock, manufacturer_name, correctCost  = prompt_add_new_item()
       if not database.manufacturer_exists(manufacturer_name):
           manufacturer_address, delivery_day, delivery_person, delivery_phone = prompt_add_manufacturer()
           database.add_new_delivery_person(delivery_person, delivery_phone)
           database.add_new_manufacturer(manufacturer_name, manufacturer_address, delivery_day, delivery_person)
       if correctCost != "Failed" and not database.item_exists(itemName):
           database.add_new_item(itemName, manufacturer_name, itemCategory, itemCost, inStock)
           print("Item successfully added to inventory!")
    elif user_input == "2":
        #deletes items from the database based on item id
        id_to_del = prompt_delete_item()
        database.delete_item(id_to_del)
    elif user_input == "3":
        #searches for items in the database
        searchedItem, searchType = prompt_search_item()
        if searchType == "Category":
            searchResult = database.search_categories(searchedItem)
            if len(searchResult) > 0:
                print_items("Searched", searchResult)
            else:
                print("No items match the search input.")
        elif searchType == "ItemName":
            searchResult = database.search_items(searchedItem)
            if len(searchResult) > 0:
                print_items("Searched", searchResult)
            else:
                print("No items match the search input.")
    elif user_input == "4":
        #views all items in the database
        all_items = database.view_items()
        print_items("All", all_items)
    elif user_input == "5":
        #updates stock for items in the database
        itemChosen, newStock = prompt_update_stock()
        if database.item_exists(itemChosen):
            database.update_stock(itemChosen, newStock)
            print("\nUpdated stock successfully!")
        else:
            print("\nNo items match the search input.")
    elif user_input == "6":
        #views all sold out items in database
        sold_out_items = database.view_sold_out_items()
        print_sold_out_items(sold_out_items)
    elif user_input == "7":
        #views the latest delivery person for an item
        item_id = prompt_select_item_for_delivery()
        if database.item_exists(item_id):
            delivery_info = database.get_delivery_person(item_id)
            print_delivery_info(delivery_info)
        else:
            print("Item not found!")
    elif user_input == "8":
        #updates the delivery person for a manufacturer
        manufacturer_name, delivery_person, delivery_phone = prompt_update_delivery_person()
        if database.manufacturer_exists(manufacturer_name):
            old_delivery_person = database.get_old_delivery_person(manufacturer_name)
            database.update_delivery_person(old_delivery_person, delivery_person, delivery_phone, manufacturer_name)
            print("\nDelivery person updated successfully!")
        else:
            print("\nNo manufacturer matches the search input.")
    else:
        print("\nInvalid input. please try again.")