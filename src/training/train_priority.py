import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

from xgboost import XGBClassifier

from src.preprocessing.embedding_generator import generate_embedding

df = pd.read_csv(
    "data/synthetic/complaints.csv"
)

X = [
    generate_embedding(text)
    for text in df["text"]
]

encoder = LabelEncoder()

y = encoder.fit_transform(df["priority"])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBClassifier()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(classification_report(y_test, predictions))

joblib.dump(model, "models/priority_model.pkl")
joblib.dump(encoder, "models/priority_encoder.pkl")