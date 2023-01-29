from typing import List, Optional

import wheel_of_learning_backend.db as tdb
from wheel_of_learning_backend.task import Task
from random import choice


def format_tasks(tasks: List[Task]):
    return "\n".join(["* " + task.name for task in tasks])


class Manager:

    TASKS_DB_NAME = 'state.json'
    DAILY_DB_NAME = 'daily.json'
    FOCUS_DB_NAME = 'focus.json'

    def __init__(self, tmp: bool = False):
        db_root = tdb.get_db_root(tmp)
        self.dbs = {
            "tasks": tdb.TinyDB(db_root + Manager.TASKS_DB_NAME),
            "daily": tdb.TinyDB(db_root + Manager.DAILY_DB_NAME),
            "focus": tdb.TinyDB(db_root + Manager.FOCUS_DB_NAME)
        }

    def add_task(self, task: Task, db_name: str) -> None:
        db = self.dbs[db_name]
        db.add_entry(task.as_mapping())

    def find_task_by_name(self, name: str, db_name="tasks") -> Optional[Task]:
        db = self.dbs[db_name]
        mapping = db.get_entry_by_name(name)
        if mapping is None:
            return None
        return Task.from_mapping(mapping)

    def delete_task_by_name(self, name: str, db_name="tasks") -> List[int]:
        db = self.dbs[db_name]
        return db.delete_entry_by_name(name)

    def get_tasks(self, db_name="tasks") -> List[Task]:
        db = self.dbs[db_name]
        tasks = [Task.from_mapping(task) for task in db.all_entries()]
        return tasks

    def select_focused_task(self) -> Optional[Task]:
        tasks = self.get_tasks("daily")
        if not tasks:
            return None
        focused_task = choice(tasks)
        db = self.dbs["focus"]
        db.delete_all_entries()
        db.add_entry(focused_task.as_mapping())
        return focused_task

    def print_tasks(self, db_name: str) -> str:
        tasks = self.get_tasks(db_name)
        if not tasks:
            return f"No tasks found in db {db_name}"
        return format_tasks(tasks)
