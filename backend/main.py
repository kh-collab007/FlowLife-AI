from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

templates = Jinja2Templates(directory = "../templates")
 
@app.get("/",response_class = HTMLResponse)
def read_root(request:Request):
    return templates.TemplateResponse(
        request = request,
        name = "index.html"
    )