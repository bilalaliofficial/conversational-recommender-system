import json
from app.utils.helpers import read_dialogue, get_conversation_by_id, read_json, read_jsonl

class DataPreprocessor:
    def __init__(self, conversation_path, data_path, item_map_path):
        self.conversation_content = read_dialogue(conversation_path)
        self.data_path = data_path
        self.item_map = read_json(item_map_path)

    def parse_conversations(self):
        return self.conversation_content

    def parse_user_data(self):
        data = read_jsonl(self.data_path)
        user_interactions = []
        for entry in data:
            user_data = json.loads(entry)
            user_id, user_info = next(iter(user_data.items()))
            conversations = user_info['Conversation']
            for conversation in conversations:
                for key, details in conversation.items():
                    dialogue = get_conversation_by_id(self.conversation_content, details["conversation_id"])
                    print("dialogue", dialogue)
                    user_interactions.append({
                        "user_id": user_id,
                        "history_interaction": user_info["history_interaction"],
                        "user_might_like": user_info["user_might_like"],
                        "dialogue": dialogue,
                        "recommendations": [self.item_map[item_id] for item_id in details["rec_item"]]
                    })
        return user_interactions