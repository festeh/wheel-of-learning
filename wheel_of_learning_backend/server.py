import fastapi
from wheel_of_learning_backend.manager import Manager
from wheel_of_learning_backend.wrapper import Wrapper
from pydantic import BaseModel


manager = Manager()
wrapper = Wrapper(manager, "server")

app = fastapi.FastAPI()


@app.get("/tasks")
async def list_tasks():
    tasks = manager.get_tasks("tasks")
    return [str(task) for task in tasks]


@app.get("/daily")
async def list_daily():
    tasks = manager.get_tasks("daily")
    return [str(task) for task in tasks]

@app.get("/focus")
async def get_focus():
    tasks = manager.get_tasks("focus")
    return [str(task) for task in tasks]

class Task(BaseModel):
    name: str

@app.post("/focus")
async def add_focus(task: Task):
    print("add_focus", task)
    manager.select_focused_task(task.name.split("\n")[0])
