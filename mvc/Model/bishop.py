from pieces import Pieces
from board import Board
import Model.Imgs 

class Bishop(Pieces):

    def __init__(self, color, location) -> None:
        super().__init__(self, color, location)
        self.img = 3



    

    def valid_move(self):
        pass


    def move_piece(self):
        pass


    def __str__(self):
        f'bishop'