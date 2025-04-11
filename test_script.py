import os
import sqlite3
from agents.memory_agent import add_customer, add_product, get_customers, get_products
from agents.recommendation_agent import recommend_products
import ollama

DB_PATH = os.path.join(os.path.dirname(__file__), "ecommerce.db")

# Test 1: Database connection
def test_database_connection():
    print("Testing database connection...")
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        conn.close()
        if tables:
            print(f"✅ Database connection successful. Tables: {tables}")
        else:
            print("⚠️ Database connected but no tables found.")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

# Test 2: Database schema check
def test_schema():
    print("Testing database schema...")
    expected_tables = {'customers', 'products'}
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = set([t[0] for t in cursor.fetchall()])
        conn.close()
        if expected_tables.issubset(tables):
            print(f"✅ All expected tables found: {expected_tables}")
        else:
            missing = expected_tables - tables
            print(f"❌ Missing tables: {missing}")
    except Exception as e:
        print(f"❌ Schema test failed: {e}")

# Test 3: Sample data in tables
def test_sample_data():
    print("Testing for sample data in tables...")
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM customers;")
        customer_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM products;")
        product_count = cursor.fetchone()[0]

        conn.close()

        print(f"✅ Customers in database: {customer_count}")
        print(f"✅ Products in database: {product_count}")

        if customer_count == 0 or product_count == 0:
            print("⚠️ Some tables have no data. Consider seeding sample data.")

    except Exception as e:
        print(f"❌ Sample data test failed: {e}")

# Test 4: Memory agent functions - Fix for add_customer
def test_add_customer():
    print("Testing add_customer function...")
    try:
        add_customer("Test User","test age", "Test Location", "test interest")
        customers = get_customers()
        if any(c[0] == 'Test User' for c in customers):  # Access by index instead of key
            print("✅ add_customer works as expected.")
        else:
            print("❌ add_customer did not add the customer properly.")
    except Exception as e:
        print(f"❌ add_customer test failed: {e}")

# Test 5: Memory agent functions - Fix for add_product
def test_add_product():
    print("Testing add_product function...")
    try:
        add_product("Test Product", "Test season", "Test Location", "Electronics")
        products = get_products()
        if any(p[0] == 'Test Product' for p in products):  # Access by index instead of key
            print("✅ add_product works as expected.")
        else:
            print("❌ add_product did not add the product properly.")
    except Exception as e:
        print(f"❌ add_product test failed: {e}")

# Test 5: Recommendation agent function - Fix for recommend_products
def test_recommendation_agent():
    print("Testing recommendation agent...")
    try:
        recommendations = recommend_products()
        if isinstance(recommendations, list):
            print(f"✅ recommend_products returned a list of {len(recommendations)} recommendations.")
        else:
            print(f"❌ recommend_products did not return a list, returned: {type(recommendations)}")
    except Exception as e:
        print(f"❌ recommend_products test failed: {e}")

# Test 6: Ollama connection test using 'mistral:latest' model
def test_ollama_connection():
    print("Testing Ollama connection using 'mistral:latest' model...")
    try:
        # Change model name to 'mistral:latest'
        response = ollama.chat(model='mistral:latest', messages=[{'role': 'user', 'content': 'Hello!'}])
        
        # Print the response to check if the model is working
        print("Ollama response:", response)
        
        # Safely access the nested dictionary for message content
        message = response.get('message', {}).get('content', '')
        
        if message:
            print(f"✅ 'mistral:latest' model responded: {message.strip()[:60]}...")  # Display first 60 characters
        else:
            print("⚠️ 'mistral:latest' model response was empty or missing expected fields.")
    except Exception as e:
        print(f"❌ Ollama connection test using 'mistral:latest' model failed: {e}")

# Test 7: Ollama sample generation test
def test_ollama_sample_generation():
    print("Testing Ollama sample generation...")
    try:
        response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': 'Hello!'}])
        
        # Log the whole response for visibility
        print("Ollama response:", response)
        
        # Safely access the nested dictionary
        message = response.get('message', {}).get('content', 'No content returned')
        
        if message:
            print(f"✅ Ollama model responded: {message.strip()[:60]}...")  # Log a truncated message
        else:
            print("⚠️ Ollama model response was empty or missing expected fields.")
    except Exception as e:
        print(f"❌ Ollama sample generation test failed: {e}")

# Run all tests
def run_all_tests():
    print("\n--- Running All Tests ---\n")
    test_database_connection()
    test_schema()
    test_sample_data()
    test_add_customer()
    test_add_product()
    test_recommendation_agent()
    test_ollama_connection()
    test_ollama_sample_generation()
    print("\n--- All Tests Completed ---")

if __name__ == "__main__":
    run_all_tests()
