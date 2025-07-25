#!/bin/bash

# Emotion Analysis API Server Startup Script

echo "🚀 Starting Emotion Analysis API Server..."
echo "📍 Server will be available at: http://localhost:8000"
echo "📚 API Documentation: http://localhost:8000/docs"
echo "🔧 Alternative docs: http://localhost:8000/redoc"
echo ""
echo "Press Ctrl+C to stop the server"
echo "=================================="

# Start the FastAPI server
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000