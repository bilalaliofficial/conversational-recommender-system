from fastapi import APIRouter, HTTPException
from app.schemas.request_schema import RequestSchema
from app.schemas.response_schema import ResponseSchema
from app.services.rag_model import RAGModel
from app.services.retriever import Retriever
from app.services.generator import Generator

router = APIRouter(prefix="", tags=["recommendation"])

@router.post("/recommendation", response_model=ResponseSchema)
async def recommendation(request: RequestSchema):
    try:
        retriever = Retriever()
        generator = Generator()
        rag_model = RAGModel(retriever, generator)
        response = rag_model.recommend(request.question, request.history)
        return {"response": response}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))