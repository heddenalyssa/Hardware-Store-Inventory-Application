import sqlite3
import queries

#this file is the main file for functions which call the sql functions
#to search, change, delete, view, etc. things for the tables

connection = sqlite3.connect("items.db")
connection.execute("PRAGMA foreign_keys = ON")

# Creating my Tables
def create_tables():
    with connection:
        connection.execute(queries.CREATE_ITEMS_TABLE)
        connection.execute(queries.CREATE_MANUFACTURER_TABLE)
        connection.execute(queries.CREATE_DELIVERY_TABLE)


#Adding new items
def add_new_item(itemName, itemManufacturer, itemCategory, itemCost, inStock):
    with connection:
        connection.execute(queries.INSERT_ITEM, (itemName, itemManufacturer, itemCategory, itemCost, inStock))


def add_new_manufacturer(manufacturerName, manufacturerAddress, deliveryDay, deliveryPerson):
    with connection:
        connection.execute(queries.INSERT_NEW_MANUFACTURER, (manufacturerName, manufacturerAddress, deliveryDay, deliveryPerson))


def add_new_delivery_person(delivery_person, delivery_phone):
    with connection:
        connection.execute(queries.INSERT_NEW_DELIVERY_PERSON, (delivery_person, delivery_phone))



#Deleting items
def delete_item(id_to_del):
    with connection:
        connection.execute(queries.DELETE_ITEM, (id_to_del, ))



#Viewing items
def view_items():
    cursor = connection.cursor()
    cursor.execute(queries.SELECT_ALL_ITEMS)
    return cursor


def view_manufacturers():
    cursor = connection.cursor()
    cursor.execute(queries.SELECT_ALL_MANUFACTURERS)
    return cursor


def view_sold_out_items():
    cursor = connection.cursor()
    cursor.execute(queries.SELECT_SOLD_OUT_ITEMS)
    return cursor.fetchall()



#Updating items
def update_stock(item_id, newStock):
    cursor = connection.cursor()
    cursor.execute(queries.UPDATE_STOCK, (newStock, item_id))
    connection.commit()
    return cursor


def update_delivery_person(old_delivery_person, delivery_person, delivery_phone, manufacturer_name):
    with connection:
        connection.execute(queries.INSERT_NEW_DELIVERY_PERSON, (delivery_person, delivery_phone, ))
        connection.execute(queries.UPDATE_MANUFACTURER_DELIVERY_PERSON, (delivery_person, manufacturer_name, ))
        connection.execute(queries.DELETE_DELIVERY_PERSON, (old_delivery_person, ))



#Searching for items
def search_items(searchedItem):
    cursor = connection.cursor()
    cursor.execute(queries.SEARCH_BY_NAME, (searchedItem,))
    return cursor.fetchall()


def search_categories(searchedItem):
    cursor = connection.cursor()
    cursor.execute(queries.SEARCH_BY_CATEGORY, (searchedItem,))
    return cursor.fetchall()



#If _____ exists
def item_exists(item_id):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_IF_ITEM_EXISTS, (item_id, ))

    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True


def manufacturer_exists(name):
    cursor = connection.cursor()
    cursor.execute(queries.CHECK_IF_MANUFACTURER_EXISTS, (name, ))

    if len(cursor.fetchall()) == 0:
        return False
    else:
        return True


#Getting items
def get_old_delivery_person(manufacturer_name):
    cursor = connection.cursor()
    cursor.execute(queries.SELECT_OLD_DELIVERY_PERSON, (manufacturer_name,))
    old_delivery_guy = cursor.fetchone()
    return old_delivery_guy[0]


def get_delivery_person(item_id):
    cursor = connection.cursor()
    cursor.execute(queries.SELECT_DELIVERY_PERSON, (item_id, ))
    return cursor.fetchall()