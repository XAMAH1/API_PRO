from database.base import *
from flask import request
import json
from random import randint
import string
from date.date import date

def create(connect):
    try:
        data = json.loads(request.data)
        command = sotrudnik.select().where(sotrudnik.c.podr == data['podraz'])
        result = connect.execute(command)
        currentsotr = False
        for i in result:
            if i[1].split('\r')[0] == data['personalfio']:
                currentsotr = True
        if currentsotr == False:
            return {
                "success": False,
                "message": "Указанного вами подразделения или сотрудника не существует"
            }
        command = visit.insert().values(type=False, department=data['podraz'], fio=data['personalfio'], dateentry=date(data['dateentry']), dateexit=date(data['dateexit']), purpose=data['purpose'])
        connect.execute(command)
        connect.commit()

        command = visit.select().where(visit.c.department == data['podraz'], visit.c.type == False, visit.c.purpose == data['purpose'], visit.c.dateentry == date(data['dateentry']), visit.c.dateentry == date(data['dateentry']), visit.c.fio == data['personalfio'])
        result = connect.execute(command)
        currentidvisit = 0
        for i in result:
            currentidvisit = i[0]
        command = personalvisit.insert().values(fio=data['fio'], phone=data['phone'], mail=data['mail'], brithday=date(data['brithday']), passport=data['passport'], visit=currentidvisit)
        connect.execute(command)
        connect.commit()
        command = personalvisit.select().where(personalvisit.c.passport == data['passport'], personalvisit.c.visit == currentidvisit)
        result = connect.execute(command)
        for i in result:
            bukv = string.ascii_letters
            login = ''
            for j in range(8):
                rand = randint(0, len(bukv))
                login += bukv[rand]
            password = ''
            for j in range(8):
                rand = randint(0, len(bukv))
                password += bukv[rand]
            command = user.insert().values(visitID=i[0], login=login, password=password, visit=False)
            connect.execute(command)
            connect.commit()
            return {
                "success": True,
                "message": "Визит успешно зарегестрирован и ожидает подтверждения",
                "data": {
                    "UserID": i[0]
                }
            }
    except Exception as e:
        print(e)
        return {
            "success": False,
            "message": "Проверьте вводимые данные"
        }