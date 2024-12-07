from app.services.retriever import Retriever
from app.services.generator import Generator
import logging

logger = logging.getLogger(__name__)

class RAGModel:
    def __init__(self, retriever: Retriever, generator: Generator):
        self.retriever = retriever
        self.generator = generator

    async def recommend(self, query, history):
        try:
            retrieved_docs = await self.retriever.retrieve(query)
        except Exception as e:
            logger.error(f"Error retrieving documents: {e}")
            raise

        try:
            response = await self.generator.generate(query, history, retrieved_docs)
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            raise

        return response
