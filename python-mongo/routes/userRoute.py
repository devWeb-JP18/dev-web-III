from fastapi import APIRouter, FastAPI
from models.userModel import User
from Controllers.Controller_user import createUser


app = FastAPI()
userAPI = APIRouter()

@userAPI.post("/criar-usuario", tags=["usuarios"])
async def insertUser(user:User):
     return createUser(user)

app.include_router(userAPI)