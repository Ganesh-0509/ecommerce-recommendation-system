# agents/product_agent.py

import sqlite3

def get_product_data():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, description, season, location FROM products")
    rows = cursor.fetchall()

    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'season': row[3],
            'location': row[4]
        })

    conn.close()
    return products
