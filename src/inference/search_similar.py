import faiss
import pandas as pd
import numpy as np

from src.preprocessing.embedding_generator import generate_embedding

index = faiss.read_index(
    "models/faiss_index.bin"
)

complaints = pd.read_csv(
    "data/synthetic/complaints.csv"
)

def search_similar(text, k=5):
    embedding = np.array([
        generate_embedding(text)
    ]).astype("float32")

    distances, indices = index.search(
        embedding,
        k
    )

    results = []

    for idx in indices[0]:
        row = complaints.iloc[idx]

        results.append({
            "complaint": row["text"],
            "category": row["category"]
        })

    return results