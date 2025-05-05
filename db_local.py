import chromadb
from chromadb.config import Settings
from chromadb import Client
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
from embedding import get_embedding
from qs import qs




# Initialize ChromaDB with persistent storage
# client = chromadb.Client(Settings(
#     chroma_db_impl="duckdb+parquet",
#     persist_directory="./chroma_db"  # local folder to store db
# ))
# collection = client.get_or_create_collection(name="institute_bangla")


# settings = Settings(
#     chroma_db_impl="duckdb+parquet",
#     persist_directory="./chroma_db"  # Path to local DB
# )

# client = Client(settings)
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("institute_bangla")



def save_documents(documents: list[str], metadatas=None):
    embeddings = [get_embedding(doc).tolist() for doc in documents]
    ids = [f"id_{i}" for i in range(len(documents))]
    collection.add(documents=documents, ids=ids, embeddings=embeddings, metadatas=metadatas or [{}])
    client.persist()  # Persist the data to disk

def query_documents(query: str, k: int = 3):
    embedding = get_embedding(query).tolist()
    results = collection.query(query_embeddings=[embedding], n_results=k)
    return results['documents'][0] if results['documents'] else []



def load_data():
    print("📥 Please Wait . Data Loading.......")
    initial= 0
    total= len(qs)
    print(f"📥 Total {total} data found. Loading data into database......")
    for data in qs:
        category = data['category']
        question = data['question']
        answer = data['answer']

        redefined_str= f"{question} | {answer}"
        save_documents([redefined_str], metadatas=[{"category": category}])
        print(f"📥 Loading {initial+1}/{total} data into database......")
        initial += 1

    print("📥 Data loaded successfully into the database.")
