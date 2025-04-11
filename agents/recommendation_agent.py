import ollama
from agents.customer_agent import get_customer_data
from agents.product_agent import get_product_data
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def generate_embedding(text):
    # Ensure response from Ollama is accessed properly
    response = ollama.embeddings(model='nomic-embed-text', prompt=text)
    return np.array(response.get('embedding', []))  # Default to an empty list if 'embedding' is missing

def recommend_products():
    customers = get_customer_data()
    products = get_product_data()

    recommendations = []

    for customer in customers:
        customer_profile = f"{customer['interests']} {customer['location']}"
        customer_embedding = generate_embedding(customer_profile)

        best_match = None
        best_similarity = -1

        for product in products:
            product_profile = f"{product['description']} {product['season']} {product['location']}"
            product_embedding = generate_embedding(product_profile)

            similarity = cosine_similarity([customer_embedding], [product_embedding])[0][0]

            if similarity > best_similarity:
                best_similarity = similarity
                best_match = product

        if best_match:
            recommendations.append({
                'customer_id': customer['id'],
                'customer_name': customer['name'],
                'recommended_product': best_match['name'],
                'similarity_score': best_similarity
            })

    return recommendations
