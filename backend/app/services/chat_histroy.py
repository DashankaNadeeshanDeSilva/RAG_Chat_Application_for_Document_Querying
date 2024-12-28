

def update_chat_history(chat_histories, user_id: str, user_content: str, bot_content: str):
    """
    Updates the in-memory chat history for a specific user.

    Args:
        user_id (str): The ID of the user.
        role (str): The role in the conversation ("user" or "bot").
        content (str): The message content.
    """
    if user_id not in chat_histories:
        chat_histories[user_id] = []
    
    # Append the user message to the chat history
    chat_histories[user_id].append({"role": "user", "content": user_content})
    # Append the bot message to the chat history
    chat_histories[user_id].append({"role": "bot", "content": bot_content})

    # Limit history length to the last 20 messages for memory efficiency
    if len(chat_histories[user_id]) > 10:
        chat_histories[user_id] = chat_histories[user_id][-10:]
