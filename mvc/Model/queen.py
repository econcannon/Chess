from pieces import Pieces

class Queen(Pieces):

    def __init__(self, color, location) -> None:
        super().__init__(self, color, location)
        self.img = 4
    
    def move_forward(self):
        rank = rank + 1