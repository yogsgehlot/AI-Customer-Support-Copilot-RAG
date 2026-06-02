from fastapi import FastAPI
from src.api.schemas import (QuestionRequest,AnswerResponse)
from src.llm.rag_pipeline import ask_rag
from src.utils.logger import logger

app = FastAPI(title="AI Customer Support Copilot",version="1.0.0")

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/ask",response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    try:
        logger.info(f"Question Received: {request.question}")
        result = ask_rag(question=request.question,history=request.history)
        logger.info(f"Answer Generated Successfully")
        return AnswerResponse(answer=result["answer"],sources=result["sources"])
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return AnswerResponse(answer=f"Error: {str(e)}",sources=[])