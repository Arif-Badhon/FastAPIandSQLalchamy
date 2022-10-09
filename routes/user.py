from fastapi import APIRouter
from database.db import conn
from model.user import *
from schemas.user import *

user = APIRouter()

@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_data(id : int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.post("/write")
async def write_data(user : User):
    conn.execute(users.insert().values(
        name = user.name,
        email = user.email,
        password = user.password
    ))
    return conn.execute(users.select()).fetchall()

@user.delete("/delete/{id}")
async def delete_user(id : int):
    return conn.execute(users.delete().where (users.c.id == id))