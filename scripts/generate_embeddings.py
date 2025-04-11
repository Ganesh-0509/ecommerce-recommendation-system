import sqlite3
import sys
import os
import logging

# Add the root directory (ecommerce) to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.embedhelper import generate_embedding, serialize_embedding

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_product_data():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description, embedding FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def generate_and_store_embeddings():
    products = get_product_data()

    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()

    for product in products:
        product_id, product_name, product_description, existing_embedding = product

        if existing_embedding:
            logging.info(f"Skipping product ID {product_id} ('{product_name}') — embedding already exists.")
            continue

        if not product_description:
            logging.warning(f"Skipping product ID {product_id} ('{product_name}') — missing description.")
            continue

        logging.info(f"Generating embedding for product ID {product_id} ('{product_name}')...")

        embedding = generate_embedding(product_description)

        if embedding is None:
            logging.warning(f"No embedding generated for product ID {product_id} ('{product_name}').")
            continue

        serialized_embedding = serialize_embedding(embedding)

        cursor.execute(
            "UPDATE products SET embedding = ? WHERE id = ?",
            (serialized_embedding, product_id)
        )
        conn.commit()

    conn.close()
    logging.info("Embeddings generation process completed successfully.")

if __name__ == "__main__":
    generate_and_store_embeddings()
