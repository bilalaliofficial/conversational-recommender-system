from pydantic import BaseModel
from typing import Any, List

class RequestSchema(BaseModel):
    question: str
    history: List[str]