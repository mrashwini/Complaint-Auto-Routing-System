import joblib

from src.preprocessing.embedding_generator import generate_embedding

model = joblib.load(
    "models/eta_model.pkl"
)

def predict_eta(text):
    embedding = generate_embedding(text)

    eta = model.predict([embedding])[0]

    return round(float(eta), 2)