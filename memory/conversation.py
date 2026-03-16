from langchain_core.chat_history import InMemoryChatMessageHistory

def create_memory():
    """Create conversation memory for interview."""
    return InMemoryChatMessageHistory()