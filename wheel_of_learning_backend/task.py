class Task:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)

    def as_mapping(self):
        return {'name': self.name}
    
    @classmethod
    def from_mapping(cls, mapping):
        return cls(mapping['name'])
