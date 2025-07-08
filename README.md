# Assignment

# 🧠 Emotion Reflection Tool

A mobile-first web application where users can enter a short text reflection (e.g., "I feel nervous about my first job interview") and receive a mock emotion analysis. Built using React + TypeScript for the frontend and FastAPI for the backend.

---

## 🚀 Features
- Clean and responsive UI with textarea input and submit button
- Sends user input to backend via POST request
- FastAPI backend returns mock emotion result
- Displays results with emotion and confidence
- Handles loading and error states

---

## 🧪 Tech Stack

### Frontend:
- React
- TypeScript
- Tailwind CSS (optional)
- Vite or Create React App

### Backend:
- FastAPI (Python)
- CORS Middleware
- Pydantic

---

## 📂 Folder Structure
```
emotion-reflection-tool/
├── backend/
│   └── main.py
├── frontend/
│   ├── src/
│   │   └── App.tsx
│   └── package.json
├── README.md
```

---

## ⚙️ Setup Instructions

### ✅ Prerequisites
- Node.js v16+
- Python 3.7+

---

## 🔧 Running the App

### 1️⃣ Backend (FastAPI)
```bash
cd backend
pip install fastapi uvicorn pydantic
uvicorn main:app --reload --port 8000
```

The backend will run at: `http://localhost:8000`

### 2️⃣ Frontend (React + TypeScript)
```bash
cd frontend
npm install
npm run dev
```

The frontend will run at: `http://localhost:3000`

> Make sure the backend is running before submitting the form.

---

## 🌐 Usage
1. Open `http://localhost:3000`
2. Enter a short reflection like:
   > "I'm feeling a little anxious about my final exams."
3. Click **Submit**
4. View the returned emotion and confidence in a styled card.

---

## 📬 API Details
### Endpoint:
```
POST /analyze
```
### Request Body:
```json
{
  "text": "I feel happy and relaxed."
}
```
### Sample Response:
```json
{
  "emotion": "Relaxed",
  "confidence": 0.92
}
```

---

---

## 📜 License
This project is for demonstration and educational purposes.
