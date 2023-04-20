import jwt
from database.base import *
from config import SECRET

def gethash(login, password):
    token = jwt.encode({"login": login, "password": password}, SECRET, algorithm="HS256")
    print(token)
    return token