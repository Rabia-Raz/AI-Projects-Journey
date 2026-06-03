
# EduAgent Inference API 🚀

An asynchronous, high-performance web service built with **FastAPI** and **Uvicorn** to productionalize AI inference for automated assessment and evaluation.

## Features 🛠️
- **Asynchronous Architecture:** Uses `async/await` handling to prevent server blocking during heavy AI processing.
- **Data Validation:** Implements `Pydantic` models for strict input-output schemas.
- **Automatic Documentation:** Instant redirection to interactive Swagger UI.
- **Performance Metrics:** Real-time tracking of request execution latency.

## How to Run 💻
1. Install dependencies: `pip install -r requirements.txt`
2. Start the production server: `python main.py`
3. Open `http://127.0.0.1:8000` to access the interactive Swagger UI dashboard.
