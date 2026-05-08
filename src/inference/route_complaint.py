import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from src.preprocessing.embedding_generator import (
    generate_embedding
)

officers = pd.read_csv(
    "data/raw/officers.csv"
)

officer_embeddings = np.load(
    "models/officer_embeddings.npy"
)

def route_complaint(text, top_k=3):

    complaint_embedding = generate_embedding(text)

    similarities = cosine_similarity(
        [complaint_embedding],
        officer_embeddings
    )[0]

    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []

    for idx in top_indices:

        officer = officers.iloc[idx]

        results.append({

            "officer_id": officer["officer_id"],

            "name": officer["name"],

            "department": officer["department"],

            "score": round(
                float(similarities[idx]),
                4
            )
        })

    return results