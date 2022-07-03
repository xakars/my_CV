from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse


router = APIRouter(
        prefix='/cv',
        tags=['Resume']
)


templates = Jinja2Templates(directory="templates")


@router.get('/python', response_class=HTMLResponse)
def get_Python_CV(request: Request):
    return templates.TemplateResponse("py_index.html", {"request": request})


@router.get('/qa', response_class=HTMLResponse)
def get_QA_CV(request: Request):
    return templates.TemplateResponse("qa_index.html", {"request": request})
