from pydantic import BaseModel
from typing import Any

class ResponseSchema(BaseModel):
    response: Any
