# Darsan Sabu George 
# 2025-04-16
# PROG2390 
# 8959922

from .connection import connection

# creating table
def create_orders_DB():
    conn = connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY,
            customer_name VARCHAR(100) NOT NULL,
            product VARCHAR(100) NOT NULL,
            quantity INT NOT NULL DEFAULT 1 CHECK (quantity >= 0),
            price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
            order_date TIMESTAMP NOT NULL DEFAULT NOW()
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()


# data insert function 
def insert_order(name, product, quantity, price):
    conn = connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO orders (customer_name, product, quantity, price)
        VALUES (%s, %s, %s, %s)
    """, (name, product, quantity, price))
    conn.commit()
    cur.close()
    conn.close()

# fetch all daat
def get_all_order_data():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
# s