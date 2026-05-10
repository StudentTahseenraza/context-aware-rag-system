conversation_memory = []

def store_memory(user_query, response):
    conversation_memory.append({
        "query": user_query,
        "response": response
    })

def retrieve_memory():
    return conversation_memory[-5:]