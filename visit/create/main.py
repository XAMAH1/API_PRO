from visit.create import personalvisit
from visit.create import groupvisit

def newvisit(connect, visit):
    if visit == 'personal':
        return personalvisit.create(connect)
    if visit == 'group':
        return groupvisit.create(connect)
    return {
        "success": False,
        "message": "Такого адреса не существует"
    }
