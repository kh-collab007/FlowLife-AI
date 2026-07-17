from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


app = FastAPI()
goals = []

templates = Jinja2Templates(directory = "../templates")
 
@app.get("/",response_class = HTMLResponse)
def read_root(request:Request):
    return templates.TemplateResponse(
        request = request,
        name = "index.html"
    )

@app.post("/submit")
def submit_goal(
    request:Request,
    goal: str = Form(...)
):
    goals.append(goal)
    return templates.TemplateResponse(
        request = request,
        name = "result.html",
        context={
            "goals":goals
        }
    )