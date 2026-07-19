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
    goal_data = {
        "id":len(goals)+1,
        "text":goal,
        "done":False
    }
    goals.append(goal_data)
    return templates.TemplateResponse(
        request = request,
        name = "result.html",
        context={
            "goals":goals
        }
    )

@app.post("/complete/{goal_id}")
def complete_goal(
    request: Request,
    goal_id: int
):
    for goal in goals:
        if goal["id"]== goal_id:
            goal["done"] = True
    return templates.TemplateResponse(
        request = request,
        name = "result.html",
        context = {
            "goals":goals
        }
    )

@app.post("/delete/{goal_id}")
def delete_goal(
    request: Request,
    goal_id: int
):
    for goal in goals:
        if goal["id"] == goal_id:
            goals.remove(goal)
            break
    return templates.TemplateResponse(
        request = request,
        name = "result.html",
        context = {
            "goals":goals
        }
    )