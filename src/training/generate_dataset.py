import pandas as pd
import random
import uuid

categories = {
    "electricity": [
        "Street light not working",
        "Power outage in sector 9",
        "Transformer damaged"
    ],
    "water": [
        "Water leakage near road",
        "No water supply",
        "Dirty water coming from tap"
    ],
    "road": [
        "Potholes on highway",
        "Road damaged after rain",
        "Traffic signal broken"
    ]
}

priorities = ["low", "medium", "high"]

rows = []

for _ in range(5000):
    category = random.choice(list(categories.keys()))

    text = random.choice(categories[category])

    rows.append({
        "complaint_id": str(uuid.uuid4()),
        "text": text,
        "category": category,
        "priority": random.choice(priorities),
        "eta_days": random.randint(1, 15),
        "officer_id": f"OFF_{random.randint(1,5)}"
    })

df = pd.DataFrame(rows)

df.to_csv(
    "data/synthetic/complaints.csv",
    index=False
)

print(df.head())