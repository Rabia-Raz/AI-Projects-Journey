from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse  # 👈 Yeh nayi line add karein
from pydantic import BaseModel, Field
from core_ai import generate_ai_response
import uvicorn
import time

app = FastAPI(
    title="Production-Ready AI Inference API",
    description="Asynchronous API for serving AI Model and RAG Inference",
    version="1.0.0"
)

# --- REQUEST & RESPONSE SCHEMAS ---
class InferenceRequest(BaseModel):
    prompt: str = Field(..., min_length=5, description="The input prompt for the AI model", examples=["What is Agentic AI?"])
    max_tokens: int = Field(default=150, ge=1, le=500, description="Limit for generated tokens")

class InferenceResponse(BaseModel):
    query: str
    response: dict
    execution_time_seconds: float

# --- ENDPOINTS ---

# 👇 Is root endpoint ko aise badal dein
@app.get("/", include_in_schema=False)
async def root():
    """
    Redirects direct traffic to the interactive Swagger documentation.
    """
    return RedirectResponse(url="/docs")


@app.post("/api/v1/predict", response_model=InferenceResponse, status_code=status.HTTP_200_OK, tags=["AI Inference"])
async def predict(payload: InferenceRequest):
    start_time = time.time()
    try:
        ai_result = await generate_ai_response(prompt=payload.prompt, max_tokens=payload.max_tokens)
        end_time = time.time()
        execution_time = round(end_time - start_time, 4)
        
        return InferenceResponse(
            query=payload.prompt,
            response=ai_result,
            execution_time_seconds=execution_time
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred during AI Inference: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)