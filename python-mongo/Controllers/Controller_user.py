from configs.db import create_mongodb_connection
from typing import List, Optional
from models.userModel import User
import uuid
from fastapi.encoders import jsonable_encoder


# Configurações de conexão com o MongoDB
connection_string = "mongodb://localhost:27017/"
database_name = "streetwise_db"
collection_name = "users"

# Criando uma conexão com o MongoDB
db = create_mongodb_connection(connection_string, database_name)
collection = db[collection_name]



def createUser(user:User)->dict:
  try:
    #user_dict = jsonable_encoder(user)  # Convertendo o objeto Pydantic em um dicionário
    #user["id"] = str(uuid.uuid4())  # Gerando um ID UUID e adicionando ao dicionário
    collection.insert_one(dict(user))
    return {"message":"usuário cadastrado com sucesso","data":user}
  except TypeError as erro:
    return{"message":"erro ao cadastrar usuário","erro":str(erro)}