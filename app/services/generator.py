from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from app.core.config import TEMPERATURE, OPENAI_API_KEY, LLM_MODEL
import logging

logger = logging.getLogger(__name__)

class Generator:
    def __init__(self):
        try:
            self.llm = ChatOpenAI(model=LLM_MODEL, temperature=TEMPERATURE, api_key=OPENAI_API_KEY)
            self.prompt_template = PromptTemplate(
                template="""You are a conversational recommender system. Use the following retrieved documents:
                {retrieved_documents}
                Based on the query: "{query}" and the conversation history: "{history}", generate a helpful response.
                """
            )
        except Exception as e:
            logger.error(f"Error initializing Generator: {e}")
            raise

    def generate(self, query, history, retrieved_docs):
        try:
            doc_contents = "\n".join([doc.page_content for doc in retrieved_docs])
            prompt = self.prompt_template.format(
                retrieved_documents=doc_contents, query=query, history=" ".join(history)
            )
            return self.llm(prompt)
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            raise
