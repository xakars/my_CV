from fastapi import FastAPI, Body, Form, Cookie
from fastapi.responses import Response
import re
from pydantic import BaseModel
from templates import templates, cv_templates
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.include_router(templates.router)
app.include_router(cv_templates.router)

class Phone(BaseModel):
    phone: str


app.mount('/img', StaticFiles(directory="img"), name="img")
app.mount('/templates/static', StaticFiles(directory="templates/static"), name="static")


@app.get("/")
def index_page():
    return {'message': 99}

