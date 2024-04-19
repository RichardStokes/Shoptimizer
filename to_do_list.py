from list_item import ListItem
from pathlib import Path

class ToDoList:


    def __init__(self, filepath=None):
        self.items = []
        self.filepath = filepath


    def load_from_file(self, filepath=None):
        path = Path(filepath) if filepath else Path(self.filepath)
        with path.open('r') as file:
            for line in file:
                list_item = ListItem(line)
                self.items.append(list_item)
        return self
    

    def add_item(self, title):
        item = ListItem(title)
        self.items.append(item)
    
    def save(self, filepath=None):
        path = Path(filepath) if filepath else Path(self.filepath)
        with path.open('w') as file:
            for each_item in self.items:
                print(each_item.title, file=file)
        return True
    