class ListItem:

    def __init__(self, title=""):
        self.title = str(title)
        self.complete = False
    

    def toggle_complete(self):
        self.complete = not self.complete