import sqlite3
from agents.memory_agent import add_customer,add_product
from agents.recommendation_agent import recommend_products

def reset_database():
    try:
        conn = sqlite3.connect('ecommerce.db')
        cursor = conn.cursor()

        # Clean customers and products
        cursor.execute("DELETE FROM customers WHERE name = 'Test User'")
        cursor.execute("DELETE FROM products WHERE name LIKE 'Test Product%'")
        cursor.execute("DELETE FROM products WHERE name IN ('Smartphone', 'Makeup Kit', 'Running Shoes')")

        conn.commit()
        print("✅ Database cleaned.")
    except Exception as e:
        print(f"❌ Error during cleanup: {e}")
    finally:
        conn.close()

def add_test_data():
    print("➕ Adding test customers...")
    add_customer("Test User", 30, "Mumbai", "Sports")
    add_customer("Test User", 32, "Delhi", "Formal wear")

    print("➕ Adding test products...")
    add_product("Winter Sports Shoes", "Durable sports shoes", "Winter", "Mumbai")
    add_product("Office Blazer", "Elegant formal blazer", "All Season", "Delhi")

    print("✅ Test data added.")

def run_recommendations():
    print("🧩 Running recommendation engine...")
    recommendations = recommend_products()

    if not recommendations:
        print("⚠️ No recommendations found.")
    else:
        print("✅ Recommendations:")
        for rec in recommendations:
            print(f"Customer {rec['customer_name']} -> {rec['recommended_product']} (Score: {rec['similarity_score']:.4f})")

if __name__ == "__main__":
    reset_database()
    add_test_data()
    run_recommendations()
