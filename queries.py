"""
Schema for tables:

items
id INTEGER PRIMARY KEY AUTOINCREMENT - the id of the item in the database
item_Name TEXT - the name of the item
manufacturer_name TEXT (FOREIGN KEY references manufacturers(manufacturer_name) - the name of the manufacturer
category TEXT - the name of the category the item belongs in
cost REAL - the cost of the item
stock INTEGER - the number of items in stock

manufacturers
manufacturer_name TEXT PRIMARY KEY - the name of the manufacturer
manufacturer_address TEXT - the address of the manufacturer
delivery_date TEXT - the day of the delivery for the manufacturer
delivery_person TEXT (FOREIGN KEY references delivery(delivery_person) - the name of the delivery person

delivery
delivery_person TEXT PRIMARY KEY - the name of the delivery person
delivery_phone TEXT - the phone number of the delivery person
"""

# create
CREATE_ITEMS_TABLE = """CREATE TABLE IF NOT EXISTS items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_Name TEXT, 
    manufacturer_name TEXT,
    category TEXT,
    cost REAL,
    stock INTEGER,
    FOREIGN KEY (manufacturer_name) REFERENCES manufacturers(manufacturer_name) ON DELETE CASCADE);"""

CREATE_MANUFACTURER_TABLE = """CREATE TABLE IF NOT EXISTS manufacturers(
    manufacturer_name TEXT PRIMARY KEY,
    manufacturer_address TEXT,
    delivery_date TEXT,
    delivery_person TEXT,
    FOREIGN KEY (delivery_person) REFERENCES delivery(delivery_person) ON UPDATE CASCADE ON DELETE CASCADE);"""

CREATE_DELIVERY_TABLE = """CREATE TABLE IF NOT EXISTS delivery(
    delivery_person TEXT PRIMARY KEY,
    delivery_phone TEXT);"""


# insert
INSERT_ITEM = "INSERT INTO items(item_Name, manufacturer_name, category, cost, stock) VALUES (?,?,?,?,?);"
INSERT_NEW_DELIVERY_PERSON = "INSERT INTO delivery(delivery_person, delivery_phone) VALUES (?,?);"
INSERT_NEW_MANUFACTURER = "INSERT INTO manufacturers(manufacturer_name, manufacturer_address, delivery_date, delivery_person) VALUES (?,?,?,?);"

# select
SELECT_ALL_ITEMS = "SELECT * FROM items;"
SELECT_ALL_MANUFACTURERS = "SELECT * FROM manufacturers;"
SELECT_OLD_DELIVERY_PERSON = "SELECT delivery_person FROM manufacturers WHERE manufacturer_name = ?;"
SELECT_SOLD_OUT_ITEMS = "SELECT items.id, items.item_NAME, manufacturers.delivery_date FROM items JOIN manufacturers ON items.manufacturer_name = manufacturers.manufacturer_name WHERE items.stock < 1;"
SELECT_DELIVERY_PERSON = ("SELECT delivery.delivery_person, delivery.delivery_phone FROM items "
                          "JOIN manufacturers ON items.manufacturer_name = manufacturers.manufacturer_name "
                          "JOIN delivery ON manufacturers.delivery_person = delivery.delivery_person "
                          "WHERE items.id = ?;")


# searches
SEARCH_BY_NAME = "SELECT id, item_Name, manufacturer_name, category, cost, stock FROM items WHERE item_Name = ?;"
SEARCH_BY_CATEGORY = "SELECT id, item_Name, manufacturer_name, category, cost, stock FROM items WHERE category = ?;"


# checks
CHECK_IF_ITEM_EXISTS = "SELECT * FROM items WHERE id = ?;"
CHECK_IF_CATEGORY_EXISTS = "SELECT category FROM items WHERE id = ?;"
CHECK_IF_MANUFACTURER_EXISTS = "SELECT * FROM manufacturers WHERE manufacturer_name = ?;"



# updates
UPDATE_STOCK = "UPDATE items SET stock = ? WHERE id = ?;"
UPDATE_MANUFACTURER_DELIVERY_PERSON= "UPDATE manufacturers SET delivery_person = ? WHERE manufacturer_name = ?;"


# deletes
DELETE_ITEM = "DELETE FROM items WHERE id = ?;"
DELETE_DELIVERY_PERSON = "DELETE FROM delivery WHERE delivery_person = ?;"

