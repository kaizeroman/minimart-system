import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='pages')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form['data']
    # Process the data with your Python code
    result = your_python_function(data)
    return render_template('index.html', result=result)

def your_python_function(data):
    # Your Python code here
    return f"Processed data: {data}"

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

if __name__ == '__main__':
    app.run(debug=True)