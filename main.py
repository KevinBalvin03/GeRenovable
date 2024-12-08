from typing import Annotated 
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

arrayConsumo = []

templateJinja = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Rutas, index, History, Qsomos, EHidrogeno, Emarina
@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templateJinja.TemplateResponse("index.html", {"request": request})

@app.get("/History", response_class=HTMLResponse)
def history(request: Request):
    return templateJinja.TemplateResponse("pages/History.html", {"request": request})

@app.get("/Qsomos", response_class=HTMLResponse)
def history(request: Request):
    return templateJinja.TemplateResponse("pages/Qsomos.html", {"request": request})

@app.get("/EHidrogeno", response_class=HTMLResponse)
def history(request: Request):
    return templateJinja.TemplateResponse("pages/EHidrogeno.html", {"request": request})

@app.get("/EMarina", response_class=HTMLResponse)
def history(request: Request):
    return templateJinja.TemplateResponse("pages/EMarina.html", {"request": request})

@app.get("/Miconsumo", response_class=HTMLResponse)
def history(request: Request):
    return templateJinja.TemplateResponse("pages/Miconsumo.html", {"request": request})

@app.post("/recibe/info")
def consumocliente(ClienteConsumo : Annotated[str, Form()]):
    return ClienteConsumo