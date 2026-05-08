import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

from xgboost import XGBRegressor

from src.preprocessing.embedding_generator import generate_embedding

df = pd.read_csv(
    "data/synthetic/complaints.csv"
)

X = [
    generate_embedding(text)
    for text in df["text"]
]

y = df["eta_days"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBRegressor()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

print("MAE:", mae)

joblib.dump(model, "models/eta_model.pkl")