import subprocess

subprocess.run(
    ["python", "-m", "src.training.generate_dataset"]
)

subprocess.run(
    ["python", "-m", "src.training.build_officer_embeddings"]
)

subprocess.run(
    ["python", "-m", "src.training.train_priority"]
)

subprocess.run(
    ["python", "-m", "src.training.train_eta"]
)

subprocess.run(
    ["python", "-m", "src.training.build_faiss"]
)

print("All models trained successfully")