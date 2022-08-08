from pieces import Pieces

class King(Pieces):

    def __init__(self, color, location) -> None:
        super().__init__(self, color, location)
        self.img = 5
    
    def move_forward(self):
        rank = rank + 1