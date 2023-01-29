import os
import tinydb


class RootPath:

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def __add__(self, other):
        return RootPath(os.path.join(self.path, other))


def get_db_root(tmp=False):
    if tmp:
        root_path = "/tmp/db"
    else:
        if not os.getenv('XDG_DATA_HOME'):
            raise Exception('XDG_DATA_HOME not set')
        root_path = os.getenv('XDG_DATA_HOME') + '/' + 'wheel-of-learning'
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    return RootPath(root_path)


class TinyDB:

    def __init__(self, db_file):
        self.db = tinydb.TinyDB(str(db_file))

    def add_entry(self, entry) -> int:
        return self.db.insert(entry)

    def get_entry_by_id(self, entry_id):
        return self.db.get(doc_id=entry_id)

    def get_entry_by_name(self, name):
        return self.db.search(tinydb.where('name') == name)

    def all_entries(self):
        return self.db.all()
