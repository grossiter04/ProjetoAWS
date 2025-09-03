# main.py
from fastapi import FastAPI
from pydantic import BaseModel

# Crie uma instância do FastAPI
app = FastAPI()

# Crie um modelo Pydantic para definir a estrutura do corpo da requisição
# Isso garante que o cliente enviará um JSON com a chave "user"
class AuthRequest(BaseModel):
    user: str

@app.get("/")
def read_root():
    return {"Status": "API is running!"}

# Crie o endpoint /auth/me com o método POST
@app.post("/auth/me")
async def auth_me(request_data: AuthRequest):
    """
    Recebe um usuário no corpo da requisição e retorna um JSON.
    """
    return {
        "user": request_data.user,
        "ping": "pong"
    }