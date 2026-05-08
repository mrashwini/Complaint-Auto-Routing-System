import pandas as pd
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

df = pd.read_csv("data/raw/officers.csv")

embeddings = []

for _, row in df.iterrows():
    profile = (
        row["department"] + " " +
        row["specialization"]
    )

    embedding = model.encode(profile)

    embeddings.append(embedding)

embeddings = np.array(embeddings)

np.save(
    "models/officer_embeddings.npy",
    embeddings
)

print("Officer embeddings saved")