from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from app.services.data_preprocessor import DataPreprocessor
import logging
from app.core.config import EMBEDDING_MODEL

logger = logging.getLogger(__name__)

class Retriever:
    def __init__(self, persist_directory="db"):
        try:
            self.embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
            self.vectorstore = Chroma(
                embedding_function=self.embeddings,
                persist_directory=persist_directory
            )
        except Exception as e:
            logger.error(f"Error initializing Retriever: {e}")
            raise

    def build_index(self, texts):
        try:
            documents = [Document(page_content=text) for text in texts]
            self.vectorstore.add_documents(documents)
        except Exception as e:
            logger.error(f"Error building index: {e}")
            raise

    async def retrieve(self, query, top_k=5):
        try:
            return self.vectorstore.similarity_search(query, k=top_k)
        except Exception as e:
            logger.error(f"Error retrieving documents: {e}")
            raise

    def build_index_from_dataset(self, conversation_path, data_path, item_map_path):
        try:
            preprocessor = DataPreprocessor(conversation_path, data_path, item_map_path)
            user_interactions = preprocessor.parse_user_data()
            texts = [interaction["dialogue"] for interaction in user_interactions]
            self.build_index(texts)
        except Exception as e:
            logger.error(f"Error building index from dataset: {e}")
            raise