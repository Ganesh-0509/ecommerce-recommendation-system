from agents.recommendation_agent import recommend_products

recommendations = recommend_products()

for rec in recommendations:
    print(f"Customer ID: {rec['customer_id']}, Name: {rec['customer_name']}, Recommended: {rec['recommended_product']}, Score: {rec['similarity_score']:.2f}")
