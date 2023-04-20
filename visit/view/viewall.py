import jwt
from flask import request
import json

from config import SECRET
from visit.view.all.group import group
from visit.view.all.personal import personal
def viewall(connect):
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
            return personal(connect)
        if data["visit"] == "group":
            return group(connect)
        return {
            "success": False,
            "message": "Проверьте вводимые данные"
        }
    except:
        return {
            "success": False,
            "message": "Проверьте вводимые данные"
        }