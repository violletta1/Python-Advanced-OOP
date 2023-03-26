class Category:
    def __init__(self, id_number: int, name: str):
        self.id = id_number
        self.name = name

    def edit(self, new_game: str):
        self.name = new_game

    def __repr__(self):
        return f"Category {self.id}: {self.name}"