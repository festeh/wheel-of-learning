import typer
from wheel_of_learning_backend.manager import Manager
from wheel_of_learning_backend.task import Task

app = typer.Typer()


def main():
    print("Hello, World!")


@app.command()
def add(task_desc: str):
    task = Task(task_desc)
    manager.add_task(task, "tasks")


@app.command()
def add_daily(task_desc: str):
    task = Task(task_desc)
    manager.add_task(task, "daily")


@app.command()
def list():
    out = manager.print_tasks("tasks")
    print(out)


@app.command()
def list_daily():
    out = manager.print_tasks("daily")
    print(out)


@app.command()
def list_focused():
    out = manager.print_tasks("focused")
    print(out)


if __name__ == "__main__":
    manager = Manager()
    app()
