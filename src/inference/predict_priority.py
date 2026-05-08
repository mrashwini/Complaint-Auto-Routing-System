import joblib

from src.preprocessing.embedding_generator import generate_embedding

model = joblib.load(
    "models/priority_model.pkl"
)

encoder = joblib.load(
    "models/priority_encoder.pkl"
)

def predict_priority(text):
    embedding = generate_embedding(text)

    prediction = model.predict([embedding])[0]

    label = encoder.inverse_transform([prediction])[0]

    return label