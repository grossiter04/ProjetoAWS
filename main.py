from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AuthRequest(BaseModel):
    user: str

@app.get("/")
def read_root():
    return {"Status": "API is running!"}

@app.post("/auth/me")
async def auth_me(request_data: AuthRequest):
    """
    Recebe um usuário no corpo da requisição e retorna um JSON.
    """
    return {
        "user": request_data.user,
        "ping": "pong"
    }