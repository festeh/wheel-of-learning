import typer

from wheel_of_learning_backend.manager import Manager
from wheel_of_learning_backend.wrapper import Wrapper

app = typer.Typer()


@app.command()
def add(task_desc: str):
    wrapper.add(task_desc)


@app.command()
def delete(task_desc: str):
    wrapper.delete(task_desc)


@app.command()
def add_daily(task_desc: str):
    wrapper.add_daily(task_desc)


@app.command()
def delete_daily(task_desc: str):
    wrapper.delete_daily(task_desc)


@app.command()
def list_tasks():
    print(manager.print_tasks("tasks"))


@app.command()
def list_daily():
    print(manager.print_tasks("daily"))


@app.command()
def list_focused():
    wrapper.list_focused()


@app.command()
def focus():
    wrapper.focus()


if __name__ == "__main__":
    manager = Manager()
    wrapper = Wrapper(manager)
    app()
