import wampconnect as wc

db = wc.DatabaseManager(conn= None, cursor=None)
try:
    db.openConnection()
    results = db.cursor.execute("SELECT * FROM product")
    
    # Print the results with added price
    for row in results:
        print(row["price"] + 20.5)
finally:
    db.closeConnection()