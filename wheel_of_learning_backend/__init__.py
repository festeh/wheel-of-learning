import logging

import typer

from wheel_of_learning_backend.manager import Manager
from wheel_of_learning_backend.task import Task

app = typer.Typer()


@app.command()
def add(task_desc: str):
    task = Task(task_desc)
    manager.add_task(task, "tasks")


@app.command()
def delete(task_desc: str):
    manager.delete_task_by_name(task_desc, "tasks")


@app.command()
def add_daily(task_desc: str):
    if manager.find_task_by_name(task_desc, "daily") is not None:
        logging.warning("Task already exists")
        return
    task = manager.find_task_by_name(task_desc, "tasks")
    if task is None:
        logging.warning("Error: cannot add daily task")
        return
    manager.add_task(task, "daily")


@app.command()
def delete_daily(task_desc: str):
    task_ids = manager.delete_task_by_name(task_desc, "daily")
    if not task_ids:
        logging.warning(f"Task {task_desc} does not exist")


@app.command()
def list_tasks():
    out = manager.print_tasks("tasks")
    print(out)


@app.command()
def list_daily():
    out = manager.print_tasks("daily")
    print(out)


@app.command()
def list_focused():
    out = manager.print_tasks("focus")
    print(out)

@app.command()
def focus():
    task = manager.select_focused_task()
    if task is None:
        logging.warning("Error: no task selected, as daily list is empty")
        return
    typer.echo(f"You are now focused on task: {task}")

if __name__ == "__main__":
    manager = Manager()
    app()
