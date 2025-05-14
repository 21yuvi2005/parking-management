import mysql.connector
from datetime import datetime

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",             # Change if your MySQL username is different
    password="2005",# 🔁 Replace this with your actual password
    database="parking_lot"
)

# Create a cursor
cursor = mydb.cursor()

# Sample data to insert
number_plate = "DL4CAF5031"
entry_time = datetime.now()

# Insert into vehicles table
sql = "INSERT INTO vehicles (number_plate, entry_time) VALUES (%s, %s)"
val = (number_plate, entry_time)
cursor.execute(sql, val)

# Commit to save changes
mydb.commit()

print(f"✅ Vehicle {number_plate} entered at {entry_time}")

# Close the connection
cursor.close()
mydb.close()
