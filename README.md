# 🛒 Ecommerce Product Recommendation System

An AI-powered recommendation system for e-commerce that uses product embeddings, cosine similarity, and intelligent agents to suggest relevant products to users.

## 🚀 Project Overview

This system is built to help e-commerce platforms recommend products to customers based on product descriptions and customer preferences.

It uses:
- **Python** for backend logic
- **Ollama AI** for generating product embeddings
- **Cosine Similarity** for finding similar products
- **SQLite** for lightweight database storage
- Modular design: Agents for customers, products, memory, and recommendations

---

## 🧩 Project Structure

ecommerce-recommendation-system/ ├── agents/ # Agents for handling product, customer, memory, and recommendations ├── scripts/ # Utility scripts (generate embeddings, etc.) │ └── generate_embedding.py ├── utils/ # Helper utilities (embedding helper, similarity helper, etc.) ├── ecommerce.db # SQLite database ├── requirements.txt # Python dependencies ├── test_script.py # Main testing script └── README.md # Project documentation



---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ecommerce-recommendation-system.git
cd ecommerce-recommendation-system

2. (Optional) Set up a virtual environment

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

3. Install dependencies

pip install -r requirements.txt

4. Ensure your database is ready

    Make sure ecommerce.db is in your project root. If needed, update the database schema manually or via setup scripts.

5. Generate embeddings for products

    python scripts/generate_embedding.py

6. Run tests and demo

    python test_script.py

🧠 How it works
    1.Product embeddings: Text descriptions of products are converted into vector embeddings using Ollama AI.

    2.Customer interactions: Customer queries and preferences are matched with product vectors.

    3.Similarity calculation: Using cosine similarity, the closest matching products are recommended.

    4.Test script: Run the end-to-end flow to see recommendations in action!

🛠️ Technologies Used
    Python 3.x

    SQLite

    Ollama AI

    Logging

    Cosine Similarity

    Modular Python architecture

✨ Features
    Automatic embedding generation for products

    Scalable architecture with agents (Product, Customer, Memory, Recommender)

    Testable system with test_script.py

    Lightweight, fast, and easy to deploy

📄 License
    This project is open-source and available under the MIT License.

🤖 Author
Your Name

If you like this project, give it a ⭐️ and share!

🙌 Contributions
Contributions are welcome!
Feel free to open issues or submit pull requests to improve the system.


---


