import os
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
