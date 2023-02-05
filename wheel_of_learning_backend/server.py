import fastapi
from wheel_of_learning_backend.manager import Manager
from wheel_of_learning_backend.wrapper import Wrapper

manager = Manager()
wrapper = Wrapper(manager, "server")


app = fastapi.FastAPI()

@app.get("/tasks")
def list_tasks():
    return wrapper.list_tasks()
