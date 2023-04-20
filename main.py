import jwt
from flask import *

from config import SECRET
from database import base
from visit.create import main
from visit.view.viewall import viewall
from visit.view.view import view
from visit.update.update import update
from auth.auth import login

app = Flask(__name__)

@app.route("/visit/create/<visit>", methods=["POST"])
def createpersonalvisit(visit):
    return main.newvisit(connect, visit)

@app.route("/visit/view/all", methods=["GET"])
def viewallvisit():
    return viewall(connect)

@app.route("/visit/view", methods=["GET"])
def viewvisit():
    return view(connect)

@app.route("/visit/update/", methods=["POST"])
def updatevisit():
    return update(connect)

@app.route("/personal/autme/<ID>", methods=["GET"])
def personal(ID):
    return login(connect, ID)

if __name__ == "__main__":
    connect = base.base()
    app.run(host="172.20.1.146", debug=True)