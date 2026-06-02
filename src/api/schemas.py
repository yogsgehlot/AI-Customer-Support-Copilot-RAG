from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str
    history: list = []


class AnswerResponse(BaseModel):
    answer: str
    sources: list[str]