from pieces import Pieces

class Pawn(Pieces):

    def __init__(self, color, location) -> None:
        super().__init__(color, location)
        self.img = 0
        self.turn = 0

    
    def append_moves(self, board):
        x = []
        if self.color == 'b':
            x.append((self.location[0] + 1, self.location[1]))
            if self.turn == 0:
                x.append((self.location[0] + 2, self.location[1]))

            #test diagonal 
            cell = board.get_cell(self.location[0] + 1, self.location[1] + 1)
            if cell != 0:
                if cell.color != self.color:
                    x.append((self.location[0] + 1, self.location + 1))
            #test other diagonal
            cell = board.get_cell(self.location[0] + 1, self.location[1] - 1)
            if cell != 0:
                if cell.color != self.color:
                    x.append((self.location[0] + 1, self.location - 1))
        
        if self.color == 'w':
            x.append((self.location[0] - 1, self.location[1]))
            if self.turn == 0:
                x.append((self.location[0] - 2, self.location[1]))

            #test diagonal 
            cell = board.get_cell(self.location[0] - 1, self.location[1] + 1)
            if cell != 0:
                if cell.color != self.color:
                    x.append((self.location[0] - 1, self.location + 1))
            #test other diagonal
            cell = board.get_cell(self.location[0] - 1, self.location[1] - 1)
            if cell != 0:
                if cell.color != self.color:
                    x.append((self.location[0] - 1, self.location - 1))
        
        for pos in x:
            if board.get_cell(pos[0], pos[1]) != 0:

                if board.get_cell(pos[0], pos[1]).color != self.color:
                    self.moves.append(pos)
                else: continue
                
            else: self.moves.append(pos)






    def __str__(self) -> str:
        return f'Pawn'