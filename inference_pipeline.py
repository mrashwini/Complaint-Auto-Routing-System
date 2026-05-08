from src.inference.route_complaint import route_complaint
from src.inference.predict_priority import predict_priority
from src.inference.predict_eta import predict_eta
from src.inference.search_similar import search_similar

def run_pipeline(text):
    officer = route_complaint(text)

    priority = predict_priority(text)

    eta = predict_eta(text)

    similar = search_similar(text)

    return {
        "complaint": text,
        "assigned_officer": officer,
        "priority": priority,
        "eta_days": eta,
        "similar_complaints": similar
    }

if __name__ == "__main__":
    complaint = input("Enter complaint: ")

    result = run_pipeline(complaint)

    print(result)