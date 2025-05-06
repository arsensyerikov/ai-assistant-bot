import sqlite3

conn = sqlite3.connect('orders.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS orders
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               email TEXT,
               service TEXT,
               comment TEXT)''')
conn.commit()

def save_order(data):
    cursor.execute("INSERT INTO orders (name, email, service, comment) VALUES (?, ?, ?, ?)", 
                   (data['name'], data['email'], data['service'], data['comment']))
    conn.commit()

def get_last_orders(limit=5):
    cursor.execute("SELECT * FROM orders ORDER BY id DESC LIMIT ?", (limit,))
    return cursor.fetchall()
