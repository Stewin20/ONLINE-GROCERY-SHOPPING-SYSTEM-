import sqlite3

def create_database():

 conn = sqlite3.connect('grocery_shop.db')

 cursor = conn.cursor()

 

 # Create tables for grocery items, users, 

and orders

 cursor.execute('''

 CREATE TABLE IF NOT EXISTS 

products (

 id INTEGER PRIMARY KEY,

 name TEXT,

 category TEXT,

 price REAL,

 image TEXT

 )''')

 cursor.execute('''

 CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,

 username TEXT,

 password TEXT

 )''')

 cursor.execute('''

 CREATE TABLE IF NOT EXISTS orders 

(

 id INTEGER PRIMARY KEY,

 user_id INTEGER,

 total REAL,

 status TEXT

 )''')

 cursor.execute('''

 CREATE TABLE IF NOT EXISTS 

order_items (

 order_id INTEGER,

 product_id INTEGER,

 quantity INTEGER

 )''')

 conn.commit()

 conn.close()

create_database();
