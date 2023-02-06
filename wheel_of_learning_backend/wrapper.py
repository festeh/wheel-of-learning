import logging
from wheel_of_learning_backend.manager import Manager
from wheel_of_learning_backend.task import Task


class Wrapper:

    def __init__(self, manager: Manager, context="cli"):
        self.manager = manager
        self.context = context

    def add(self, task_desc: str):
        task = Task(task_desc)
        self.manager.add_task(task, "tasks")

    def delete(self, task_desc: str):
        self.manager.delete_task_by_name(task_desc, "tasks")

    def add_daily(self, task_desc: str):
        if self.manager.find_task_by_name(task_desc, "daily") is not None:
            logging.warning("Task already exists")
            return
        task = self.manager.find_task_by_name(task_desc, "tasks")
        if task is None:
            logging.warning("Error: cannot add daily task")
            return
        self.manager.add_task(task, "daily")

    def delete_daily(self, task_desc: str):
        task_ids = self.manager.delete_task_by_name(task_desc, "daily")
        if not task_ids:
            logging.warning(f"Task {task_desc} does not exist")

    def list_tasks(self):
        if self.context == "cli":
            return []
        tasks = self.manager.get_tasks("tasks")
        return [str(task) for task in tasks]

    def list_daily(self):
        out = self.manager.print_tasks("daily")
        print(out)

    def list_focused(self):
        out = self.manager.print_tasks("focus")
        print(out)

    def focus(self):
        task = self.manager.select_focused_task()
        if task is None:
            logging.warning("Error: no task selected, as daily list is empty")
            return
        print(f"You are now focused on task: {task}")
