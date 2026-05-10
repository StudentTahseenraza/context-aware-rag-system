from fastapi import FastAPI
from rag_pipeline import generate_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Context-Aware RAG System Running"}

@app.post("/chat")
def chat(query: str):
    response = generate_response(query)
    return {"response": response}