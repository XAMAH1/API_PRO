from database.base import *

def group(connect, data):
    try:
        command = groupvisit.select().where(groupvisit.c.visitID == data["ID"])
        result = connect.execute(command)
        for i in result:
            command = visit.update().where(visit.c.id == i[6]).values({"result": data["result"], "answer": data["answer"]})
            connect.execute(command)
            connect.commit()
            return {
                "success": True,
                "message": "Данные успешно изменены"
            }
    except:
        return {
            "success": False,
            "message": "Проверьте вводимые данные"
        }