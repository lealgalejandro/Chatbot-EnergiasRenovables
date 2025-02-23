from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import get_response
from pydantic import BaseModel

app = FastAPI()

#Configuramos los CORS para que permita el acceso desde el front
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = get_response(request.message)
    return {"response": response}

@app.get("/")
def home():
    return {"message":"Chatbot de Cambio climatico y Energias Renovables"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)