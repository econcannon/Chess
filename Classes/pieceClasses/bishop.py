class Bishop:

    def __init__(self, rank) -> None:
        self.rank = rank
    
    def move_forward(self):
        rank = rank + 1