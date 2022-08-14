from pieces import Pieces

class Pawn(Pieces):

    def __init__(self, color, location) -> None:
        super().__init__(self, color, location)
        self.img = 0
        self.turn = 0

    
    def append_moves(self):
        move_1, move_2 = 0, 0
        if self.turn == 0:
            if self.color == 'w':
                move_2 = self.location[0] - 2, self.location[1]

            else:
                move_2 = self.location[0] + 2, self.location[1]

        if self.color == 'w':
            move_1 = self.location[0] - 1, self.location[1]
        else:
            move_1 = self.location[0] + 1, self.location[1]
        
        if move_1:
            self.moves.append(move_1)
        if move_2:
            self.moves.append(move_2)
