from database.base import *
from flask import request
import json
from random import randint
import string
from date.date import date
from auth.reg import gethash

def create(connect):
    data = json.loads(request.data)     # Преобразование body в json
    command = sotrudnik.select().where(sotrudnik.c.podr == data['podraz'])  # Создание комманды для выборки сотрудника по подразделению
    result = connect.execute(command)   # Выполнение комманды
    currentsotr = False     # Создание переменной для проверки
    for i in result:
        if i[1].split('\r')[0] == data['personalfio']:  # Проверка на наличие введенного сотрудника
            currentsotr = True  # Изменение переменной для проверки
    if currentsotr == False:    # Проверка переменной
        return {
            "success": False,
            "message": "Указанного вами подразделения или сотрудника не существует"
        }   # Возврат ошибки
    command = visit.insert().values(type=True, department=data['podraz'], fio=data['personalfio'],
                                    dateentry=date(data['dateentry']), dateexit=date(data['dateexit']),
                                    purpose=data['purpose'], group=data['group'])   # Создание команды для добавления новой записи в таблицу "visit"
    connect.execute(command)    # Выполнение команды
    connect.commit()    # Сохранение изменений

    command = visit.select().where(visit.c.department == data['podraz'], visit.c.type == True,
                                   visit.c.purpose == data['purpose'], visit.c.dateentry == date(data['dateentry']),
                                   visit.c.dateentry == date(data['dateentry']), visit.c.fio == data['personalfio'], visit.c.group == data['group'])    # Создание
    result = connect.execute(command)
    currentidvisit = 0
    for i in result:
        currentidvisit = i[0]
    command = groupvisit.insert().values(fio=data['fio'], phone=data['phone'], mail=data['mail'], brithday=date(data['brithday']), passport=data['passport'], visit=currentidvisit)
    connect.execute(command)
    connect.commit()
    command = groupvisit.select().where(groupvisit.c.passport == data['passport'], groupvisit.c.visit == currentidvisit)
    result = connect.execute(command)
    for i in result:
        bukv = string.ascii_letters
        login = ''
        for j in range(8):
            rand = randint(0, len(bukv)-1)
            login += bukv[rand]
        password = ''
        for j in range(8):
            rand = randint(0, len(bukv)-1)
            password += bukv[rand]

        hashlog = gethash(login, password)
        command = user.insert().values(visitID=i[0], hashlogin=hashlog, visit=True)
        connect.execute(command)
        connect.commit()
        return {
            "success": True,
            "message": "Визит успешно зарегестрирован и ожидает подтверждения",
            "data": {
                "UserID": i[0], "login": login, "password": password
            }
        }