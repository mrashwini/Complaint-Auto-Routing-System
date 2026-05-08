

# 🚀 Complaint Auto-Routing System

### AI/ML-powered multilingual complaint routing platform with semantic search, priority prediction, ETA estimation, and audio complaint support.


---

# 📌 Overview

Complaint Auto-Routing System is an end-to-end AI/ML platform that intelligently processes public complaints submitted through multilingual text or audio.

The system automatically:

✅ Routes complaints to the most relevant officer  
✅ Predicts complaint priority (High / Medium / Low)  
✅ Estimates expected resolution time  
✅ Finds semantically similar historical complaints  
✅ Supports multilingual and audio complaints  
✅ Works fully offline without external APIs  

---

# ✨ Features

## 🧠 AI Features

- Semantic Officer Routing
- Priority Classification
- ETA Prediction
- Similar Complaint Retrieval
- Audio Complaint Transcription
- Multilingual Complaint Understanding

---

# 🏗️ System Architecture

```text
Complaint Input
(Text / Audio)
        ↓
Whisper Transcription
        ↓
Text Preprocessing
        ↓
Embedding Generation
        ↓
├── Officer Routing
├── Priority Prediction
├── ETA Estimation
└── Similarity Search
        ↓
Final AI Predictions

# ▶️ How To Run The Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/mrashwini/Complaint-Auto-Routing-System.git
```

---

## 2️⃣ Navigate To Project Folder

```bash
cd Complaint-Auto-Routing-System
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install FFmpeg (Required For Audio Support)

### Windows

```bash
winget install ffmpeg
```

---

## 5️⃣ Train Models

```bash
python train_all.py
```

This generates:
- Priority prediction model
- ETA prediction model
- Officer embeddings
- FAISS similarity index

---

## 6️⃣ Run Streamlit Application

```bash
streamlit run app/streamlit_app.py
```

---

## 7️⃣ Open Browser

Streamlit automatically opens:

```text
http://localhost:8501
```

---

# 🧪 Testing The System

## Example Text Complaint

```text
Street light not working near bus stand
```

---

## Example Audio Complaint

Upload a `.wav` or `.mp3` file saying:

```text
Water leakage near market road
```