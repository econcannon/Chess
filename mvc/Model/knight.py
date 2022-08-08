from pieces import Pieces

class Knight(Pieces):

    def __init__(self, color, location) -> None:
        super().__init__(self, color, location)
        self.img = 2
    
    def move_forward(self):
        rank = rank + 1