from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Body, Form, Cookie
from pydantic import BaseModel
from fastapi.responses import Response
import re
from typing import Optional


router = APIRouter(
        prefix='/get_phone',
        tags=['PhoneUnify'],
)

class Phone(BaseModel):
    phone: str


def unify(phone: str):
    num = re.sub("[^0-9]", "", phone)
    if len(num) < 10 or len(num) > 11 or num[-10] != '9':
        return phone
    phone_num = "8 (9{}{}) {}{}{}-{}{}-{}{}".format(*num[-9:])
    return phone_num

@router.post("/unify_phone_from_json")
def unify_phone_from_querty(phone : Phone):
    """
    API обрабатывает HTTP POST запросы и принимает телефон в теле запроса в виде JSON, далее
    стандартизировав принятый телефон, сервис просто возвращает его.

    **Например**

    - input >>  {"phone": "89876543210"}
    - output >> 8 (987) 654-32-10
    """
    return Response(unify(phone.phone))

@router.post("/unify_phone_from_form")
def unify_from_form_data(phone: Phone = Form(...)):
    """
    API обрабатывает HTTP POST запросы и принимает телефон в теле Form Data, далее 
    стандартизировав принятый телефон, сервис просто возвращает его.
    
    **Например**

    - input >>  {"phone": "89876543210"}
    - output >> 8 (987) 654-32-10
    """
    return Response(unify(phone.phone))


@router.get("/unify_phone_from_cookies")
def unify_phone_from_cookies(phone: Optional[str] = Cookie(None)):
    return Response(unify(phone))


@router.get("/unify_phone_from_query")
def unify_phone_from_query(phone : str):
    return Response(unify(phone))

