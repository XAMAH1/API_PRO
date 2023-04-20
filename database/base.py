from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import mysql

from config import PASSWORDBASE

meta = MetaData()
engine = create_engine("mysql+mysqlconnector://ilya:%s@berrypay.ru:3306/ilya" % (PASSWORDBASE))
session = sessionmaker(bind=engine)

user = Table("user", meta,
    Column("ID", Integer, primary_key=True),
    Column("visitID", Integer),
    Column("login", String(100), nullable=False),
    Column("password", String(100), nullable=False),
    Column("visit", Boolean, nullable=False)
)

visit = Table("visit", meta,
              Column("id", Integer, nullable=False, primary_key=True),
              Column("type", Boolean, nullable=False),
              Column("department", String(100), nullable=False),
              Column("fio", String(100), nullable=False),
              Column("dateentry", Date),
              Column("dateexit", Date),
              Column("purpose", String(100), nullable=False),
              Column("group", String(100), default="Отсутвует"),
              Column("result", Integer, nullable=False, default=0),
              Column("answer", String(200), nullable=False, default="Ожидает подтверждения")
              )

personalvisit = Table("personalvisit", meta,
    Column("visitID", Integer, primary_key=True),
    Column("fio", String(100), nullable=False),
    Column("phone", String(20)),
    Column("mail", String(100)),
    Column("brithday", String(15), nullable=False),
    Column("passport", String(20), nullable=False),
    Column("visit", Integer, nullable=False)
)

groupvisit = Table("groupvisit", meta,
    Column("visitID", Integer, primary_key=True),
    Column("fio", String(100), nullable=False),
    Column("phone", String(20)),
    Column("mail", String(100)),
    Column("brithday", String(15), nullable=False),
    Column("passport", String(20), nullable=False),
    Column("visit", Integer, nullable=False)
)

sotrudnik = Table("personal", meta,
                  Column("ID", Integer),
                  Column("fio", String(100)),
                  Column("podr", String(50)),
                  Column("department", String(50)),
)

def base():
    meta.create_all(engine)
    connect = engine.connect()
    print("Base connect")
    return connect
