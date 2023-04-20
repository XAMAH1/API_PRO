import jwt
from database.base import *
from config import SECRET

def login(connect, id):
    command = sotrudnik.select().where(sotrudnik.c.ID == int(id))
    result = connect.execute(command)
    for i in result:
        token = jwt.encode({"ID": id, "fio": i[1], "podr": i[2], "department": i[3]}, SECRET, algorithm="HS256")
        return {
            "success": True,
            "message": token
        }
    return {
        "success": False,
        "message": "Сотрудник с таким ID не найден"
    }