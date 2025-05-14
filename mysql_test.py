import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2005",
        database="carparking"
    )
    print("✅ Connection successful!")
except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
 