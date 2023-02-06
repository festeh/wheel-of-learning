import fastapi
from wheel_of_learning_backend.manager import Manager
from wheel_of_learning_backend.wrapper import Wrapper

manager = Manager()
wrapper = Wrapper(manager, "server")

app = fastapi.FastAPI()


@app.get("/tasks")
def list_tasks():
    tasks = manager.get_tasks("tasks")
    return [str(task) for task in tasks]


@app.get("/daily")
def list_daily():
    tasks = manager.get_tasks("daily")
    return [str(task) for task in tasks]
