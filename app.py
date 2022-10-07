from turtle import title
from fastapi import FastAPI



app = FastAPI(
    title = "FastAPI implementation with SQLAlchamey",
    description = "Testing for the use"
)

@app.get("/")
def root():
    return ({"msg" : "working"})