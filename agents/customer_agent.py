# agents/customer_agent.py

import sqlite3

def get_customer_data():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, age, location, interests FROM customers")
    rows = cursor.fetchall()

    customers = []
    for row in rows:
        customers.append({
            'id': row[0],
            'name': row[1],
            'age': row[2],
            'location': row[3],
            'interests': row[4].split(',')  # interests stored as comma-separated
        })

    conn.close()
    return customers
