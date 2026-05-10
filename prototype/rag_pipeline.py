from embeddings import generate_embedding

memory_store = []

def retrieve_context(query_embedding):
    if not memory_store:
        return "No previous context available."
    
    return memory_store[-1]

def generate_response(query):
    embedding = generate_embedding(query)

    context = retrieve_context(embedding)

    response = f"""
    Retrieved Context:
    {context}

    AI Response:
    This is a prototype response generated using contextual retrieval.
    """

    memory_store.append(query)

    return response