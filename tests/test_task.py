import random
import string

import wheel_of_learning_backend.task as task
from wheel_of_learning_backend.db import TinyDB, get_db_root


def test_task_2():
    my_task = task.Task("read a book")
    assert str(my_task) == "read a book"


def rand_name():
    return "".join(random.choices(string.ascii_letters + string.digits, k=10))


def test_db():
    db_name = rand_name() + ".json"
    db_path = get_db_root(True) + db_name
    tinydb = TinyDB(db_path)
    id = tinydb.add_entry({"name": "test_name", "value": "test_value"})
    assert tinydb.get_entry_by_id(id) == {"name": "test_name", "value": "test_value"}
