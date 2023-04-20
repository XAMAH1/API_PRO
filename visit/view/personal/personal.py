from database.base import *

def personal(connect, data):
    command = personalvisit.select().where(personalvisit.c.visitID == data['ID'])
    result = connect.execute(command)
    for i in result:
        command = visit.select().where(visit.c.id == i[6])
        currentresult = connect.execute(command)
        for j in currentresult:
            return {"user": {"id": i[0], "fio": i[1], "phone": i[2], "mail": i[3], "brithday": i[4], "passport": i[5]},
                                 "purpose": {"purpose": j[6], "dateentry": j[4], "dateexit": j[5], "podraz": j[2],
                                 "fio": j[3], "result": j[8], "answer": j[9], "visit": "group"}, "success": True}
    return {
        "success": False,
        "message": "Пользователь с таким ID не найден"
    }