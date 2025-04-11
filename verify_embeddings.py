import sqlite3

# Check the structure of the 'products' table
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Check the columns in the products table
cursor.execute("PRAGMA table_info(products);")
columns = cursor.fetchall()
print("Table structure:")
for column in columns:
    print(column)

# Check if embeddings are populated
cursor.execute("SELECT id, name, embedding FROM products LIMIT 5;")
products = cursor.fetchall()

print("\nProduct Data with Embeddings:")
for product in products:
    print(product)

# Optionally, you can deserialize an embedding to check its content
from utils.embedhelper import deserialize_embedding

print("\nDeserialized Embedding Example:")
cursor.execute("SELECT embedding FROM products WHERE id = 1;")
result = cursor.fetchone()
serialized_embedding = result[0]
embedding = deserialize_embedding(serialized_embedding)
print(embedding)

conn.close()
    