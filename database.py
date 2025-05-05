import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
from embedding import get_embedding
import random

client = chromadb.Client()
collection = client.get_or_create_collection(name="institute_bangla")

def save_documents(documents: list[str], metadatas=None):
    print("---------------------------------------------------------------------------------------")
    print("Embeddings :")
    print(get_embedding(documents[0]).tolist())
    
    embeddings = [get_embedding(doc).tolist() for doc in documents]
    ids = [f"id_{random.randint(1,100000)}" for i in range(len(documents))]
    collection.add(documents=documents, ids=ids, embeddings=embeddings, metadatas=metadatas or [{}])

def query_documents(query: str, k: int = 3):
    embedding = get_embedding(query).tolist()
    results = collection.query(query_embeddings=[embedding], n_results=k) 
    print("---------------------------------------------------------------------------------------")
    print("Collections :")
    print(collection.get())
    print("\n\n\n")
    return results['documents'][0] if results['documents'] else [] 
