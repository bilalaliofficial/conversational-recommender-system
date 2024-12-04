"""Script to generate embeddings from conversation data."""

import logging
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from app.services.retriever import Retriever

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def validate_paths(*paths: str) -> bool:
    """Validate that all required files exist."""
    for path in paths:
        if not Path(path).exists():
            logger.error(f"Required file not found: {path}")
            return False
    return True

def main() -> None:
    """Generate embeddings from conversation data."""
    try:
        # Define data paths
        conversation_path = "data/LLM_Redial/Conversation.txt"
        data_path = "data/LLM_Redial/final_data.jsonl"
        item_map_path = "data/LLM_Redial/item_map.json"

        # Validate input files
        if not validate_paths(conversation_path, data_path, item_map_path):
            sys.exit(1)

        logger.info("Initializing retriever and building index...")
        retriever = Retriever()
        retriever.build_index_from_dataset(conversation_path, data_path, item_map_path)
        
        logger.info("Index built and persisted successfully.")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()