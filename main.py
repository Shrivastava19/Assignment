from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime

app = FastAPI(title="Emotion Analysis API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class EmotionInput(BaseModel):
    text: str

class EmotionRecord(BaseModel):
    id: str
    text: str
    emotion: str
    confidence: float
    created_at: datetime
    updated_at: datetime

class EmotionResponse(BaseModel):
    id: str
    text: str
    emotion: str
    confidence: float
    created_at: datetime
    updated_at: datetime

class EmotionUpdate(BaseModel):
    text: Optional[str] = None
    emotion: Optional[str] = None
    confidence: Optional[float] = None

# In-memory storage (in production, use a database)
emotion_records = {}

# Mock emotion analysis function
def analyze_emotion(text: str) -> tuple[str, float]:
    emotions = [
        ("Happy", 0.92),
        ("Sad", 0.88),
        ("Anxious", 0.85),
        ("Excited", 0.90),
        ("Angry", 0.78),
        ("Relaxed", 0.95),
        ("Confused", 0.82)
    ]
    # Simple mock logic based on text length
    index = len(text) % len(emotions)
    return emotions[index]

# CRUD Operations

# CREATE - Add new emotion analysis
@app.post("/emotions", response_model=EmotionResponse)
def create_emotion_analysis(input_data: EmotionInput):
    """Create a new emotion analysis record"""
    emotion, confidence = analyze_emotion(input_data.text)
    
    record_id = str(uuid.uuid4())
    now = datetime.now()
    
    record = EmotionRecord(
        id=record_id,
        text=input_data.text,
        emotion=emotion,
        confidence=confidence,
        created_at=now,
        updated_at=now
    )
    
    emotion_records[record_id] = record
    return record

# READ - Get all emotion records
@app.get("/emotions", response_model=List[EmotionResponse])
def get_all_emotions():
    """Get all emotion analysis records"""
    return list(emotion_records.values())

# READ - Get specific emotion record by ID
@app.get("/emotions/{record_id}", response_model=EmotionResponse)
def get_emotion_by_id(record_id: str):
    """Get a specific emotion analysis record by ID"""
    if record_id not in emotion_records:
        raise HTTPException(status_code=404, detail="Emotion record not found")
    return emotion_records[record_id]

# UPDATE - Update existing emotion record
@app.put("/emotions/{record_id}", response_model=EmotionResponse)
def update_emotion_record(record_id: str, update_data: EmotionUpdate):
    """Update an existing emotion analysis record"""
    if record_id not in emotion_records:
        raise HTTPException(status_code=404, detail="Emotion record not found")
    
    record = emotion_records[record_id]
    
    # Update fields if provided
    if update_data.text is not None:
        record.text = update_data.text
        # Re-analyze emotion if text changed
        emotion, confidence = analyze_emotion(update_data.text)
        record.emotion = emotion
        record.confidence = confidence
    
    if update_data.emotion is not None:
        record.emotion = update_data.emotion
    
    if update_data.confidence is not None:
        record.confidence = update_data.confidence
    
    record.updated_at = datetime.now()
    emotion_records[record_id] = record
    
    return record

# DELETE - Delete emotion record
@app.delete("/emotions/{record_id}")
def delete_emotion_record(record_id: str):
    """Delete an emotion analysis record"""
    if record_id not in emotion_records:
        raise HTTPException(status_code=404, detail="Emotion record not found")
    
    del emotion_records[record_id]
    return {"message": f"Emotion record {record_id} deleted successfully"}

# Legacy endpoint for backward compatibility
@app.post("/analyze")
def analyze(input_data: EmotionInput):
    """Legacy endpoint - creates and returns emotion analysis"""
    emotion, confidence = analyze_emotion(input_data.text)
    return {
        "emotion": emotion,
        "confidence": confidence
    }

# Health check endpoint
@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "total_records": len(emotion_records),
        "timestamp": datetime.now()
    }