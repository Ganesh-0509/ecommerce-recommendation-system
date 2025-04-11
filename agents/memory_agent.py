from database.db import create_connection
from utils.embedhelper import generate_embedding, serialize_embedding
import sqlite3

def add_customer(name, age, location, interests):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO customers (name, age, location, interests)
        VALUES (?, ?, ?, ?)
    ''', (name, age, location, interests))

    conn.commit()
    conn.close()

def add_product(name, description, season, location):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    product_profile = f"{description} {season} {location}"
    embedding = generate_embedding(product_profile)

    if embedding:  # Check to avoid None issues
        serialized_embedding = serialize_embedding(embedding)
    else:
        serialized_embedding = ''

    cursor.execute('''
        INSERT INTO products (name, description, season, location, embedding)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, description, season, location, serialized_embedding))

    conn.commit()
    conn.close()

def get_customers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    conn.close()
    return rows
