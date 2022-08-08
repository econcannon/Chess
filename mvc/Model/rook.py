from pieces import Pieces

class Rook(Pieces):

    def __init__(self, color, location) -> None:
        super().__init__(self, color, location)
        self.img = 1


    def move_forward(self):
        rank = rank + 1