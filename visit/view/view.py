import jwt
from flask import request
import json

from config import SECRET
from visit.view.personal import personal
from visit.view.group import group

def view(connect):
    try:
        try:
            jwt.decode(request.headers["Authorization"].split(" ")[1], SECRET, algorithms="HS256")
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