import wheel_of_learning_backend.db as db
from wheel_of_learning_backend.task import Task
from typing import List


def format_tasks(tasks: List[Task]):
    return "\n".join(["* " + task.name for task in tasks])


class Manager:

    TASKS_DB_NAME = 'state.json'
    DAILY_DB_NAME = 'daily.json'
    FOCUS_DB_NAME = 'focus.json'

    def __init__(self, tmp: bool = False):
        kek = tmp + 1
        print(kek)

        db_root = db.get_db_root(tmp)
        self.dbs = {
            "tasks": db.TinyDB(db_root + Manager.TASKS_DB_NAME),
            "daily": db.TinyDB(db_root + Manager.DAILY_DB_NAME),
            "focus": db.TinyDB(db_root + Manager.FOCUS_DB_NAME)
        }

    def add_task(self, task: Task, db_name: str) -> None:
        db = self.dbs[db_name]
        db.add_entry(task.as_mapping())

    def find_task(self, name: str) -> Task:
        db = self.dbs["tasks"]
        return Task.from_mapping(db.get(name))

    def print_tasks(self, db_name: str) -> str:
        db = self.dbs[db_name]
        tasks = [Task.from_mapping(m) for m in db.all_entries()]
        if not tasks:
            return f"No tasks found in db {db_name}"
        return format_tasks(tasks)
