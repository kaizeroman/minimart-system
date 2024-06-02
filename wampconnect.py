import mysql.connector

class DatabaseManager:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    # Connect to the MySQL database
    def openConnection(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="minimart"
        )
        # Create a cursor object
        cursor = self.conn.cursor(dictionary=True)

    # Close the cursor and connection
    def closeConnection(self):
        self.cursor.close()
        self.conn.close()