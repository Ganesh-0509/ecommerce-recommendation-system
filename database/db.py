# database/db.py
import sqlite3
def create_connection():
    return sqlite3.connect('ecommerce.db')

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            location TEXT,
            interests TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            season TEXT,
            location TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_embeddings (
            customer_id INTEGER PRIMARY KEY,
            embedding BLOB
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product_embeddings (
            product_id INTEGER PRIMARY KEY,
            embedding BLOB
        )
    ''')

    conn.commit()
    conn.close()

def insert_sample_data():
    from agents.memory_agent import add_product
    conn = create_connection()
    cursor = conn.cursor()

    customers = [
        (1, 'John Doe', 30, 'New York', 'electronics,gaming,fitness'),
        (2, 'Jane Smith', 25, 'California', 'fashion,beauty,travel')
    ]
    cursor.executemany('INSERT OR IGNORE INTO customers VALUES (?, ?, ?, ?, ?)', customers)

    conn.commit()
    conn.close()

    # use add_product to insert products properly
    add_product('Smartphone', 'Latest smartphone with advanced features', 'summer', 'New York')
    add_product('Running Shoes', 'Comfortable and durable running shoes', 'summer', 'California')
    add_product('Makeup Kit', 'Complete makeup kit for daily use', 'all', 'California')

if __name__ == "__main__":
    create_tables()
    insert_sample_data()
    print("Database setup completed.")
