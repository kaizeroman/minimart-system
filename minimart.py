import mysql.connector

cursor = None
conn = None

    # Connect to the MySQL database
def openConnection():
    global conn, cursor
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="minimart"
    )
    # Create a cursor object
    cursor = conn.cursor(dictionary=True)

# Close the cursor and connection
def closeConnection():
    global conn, cursor
    cursor.close()
    conn.close()

openConnection()
cursor.execute("SELECT * FROM product")
results = cursor.fetchall()
print(results)
closeConnection()