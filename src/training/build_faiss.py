import faiss
import numpy as np
import pandas as pd

from src.preprocessing.embedding_generator import generate_embedding

df = pd.read_csv(
    "data/synthetic/complaints.csv"
)

embeddings = np.array([
    generate_embedding(text)
    for text in df["text"]
]).astype("float32")

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(embeddings)

faiss.write_index(
    index,
    "models/faiss_index.bin"
)

print("FAISS index saved")