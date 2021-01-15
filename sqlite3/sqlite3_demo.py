# Getting Started with sqlite3 Databases
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

import sqlite3

# Connect to database
conn = sqlite3.connect("demo.db")

# Create a cursor object
c = conn.cursor()

# Create table
# sql = "CREATE TABLE contacts (name text, phone text, city text)"
# c.execute(sql)

# Insert values
# sql = "INSERT INTO contacts VALUES ('Jenny','867-5309', 'Los Angeles')"
# c.execute(sql)

# Update values
# sql = "UPDATE contacts SET city='Dallas' WHERE name='Jenny'" 
# c.execute(sql)

# Retrieve values
# sql = "SELECT * FROM contacts WHERE name='Jenny'"
# c.execute(sql)

# results = c.fetchall()
# print(results)

# Commit changes
conn.commit()

# Close connection
conn.close()
