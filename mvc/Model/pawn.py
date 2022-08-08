from pieces import Pieces

class Pawn(Pieces):

    def __init__(self, color, location) -> None:
        super().__init__(self, color, location)
        self.img = 0
    
    def move_forward(self):
        rank = rank + 1