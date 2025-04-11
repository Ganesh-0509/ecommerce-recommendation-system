import ollama

def generate_embedding(text):
    try:
        response = ollama.embeddings(model='mistral', prompt=text)
        embedding = response['embedding']
        return embedding
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return None

def serialize_embedding(embedding):
    return ','.join(map(str, embedding))

def deserialize_embedding(serialized_embedding):
    return list(map(float, serialized_embedding.split(',')))
