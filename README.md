Project:
This is an inventory system application for a hardware store.

Database Design:
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


I chose this design the way I did because it separates the item, manufacturer, and the delivery information, using only the necessary foreign key relationships as overlapping information. Each table focuses on one area of the database, which improves modularity and clarity. The items table tracks product details such as name, category, cost, and stock, while linking each item to its manufacturer via a foreign key. The manufacturer's table stores name, address, and delivery date, and connects to the delivery person through another foreign key. The delivery table has contact details for delivery staff. This design allows for easy data management and understanding, and can be expanded in the future if needed.

Software Design: 

The way I chose to design the software promotes modularity and makes the main file easy to read and understand. My overall architecture of the program is having a main menu that the user navigates, and depending on what the user chooses in the menu, the program calls functions to complete those tasks. 
