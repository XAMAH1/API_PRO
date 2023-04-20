from flask import request
import json
import jwt

from config import SECRET
from visit.update.group import group
from visit.update.personal import personal

def update(connect):
    try:
        try:
            user = jwt.decode(request.headers["Authorization"].split(" ")[1], SECRET, algorithms="HS256")
        except:
            return {
                "success": False,
                "message": "Неверный токен"
            }
        data = json.loads(request.data)
        if data["visit"] == "personal":
            return personal.personal(connect, data)
        if data["visit"] == "group":
            return group.group(connect, data)
    except:
        return {
            "success": False,
            "message": "Проверьте вводимые данные"
        }