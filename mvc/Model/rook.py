from mvc.Model.pieces import Pieces

class Rook(Pieces):

    def __init__(self, color, location) -> None:
        #self.color = color
        #self.location = location
        super().__init__(color, location)
        self.img = 1
        self.turn = 0


    def append_moves(self, board):
        
        self.moves = []        
        #Move to top
        for i in range(1,8):

            x = self.location[0] + i, self.location[1]
            if (x[0] > 7) or (x[1] > 7) or (x[0] < 0) or (x[1] < 0):
                break

            if board.get_cell(x[0], x[1]) != 0:
                if board.get_cell(x[0], x[1]).color != self.color:
                    self.moves.append(x)
                    break
                else: break
            
            else: self.moves.append(x)

        #Move to left
        for i in range(1,8):

            x = self.location[0], self.location[1] - i
            if (x[0] > 7) or (x[1] > 7) or (x[0] < 0) or (x[1] < 0):
                break

            if board.get_cell(x[0], x[1]) != 0:
                if board.get_cell(x[0], x[1]).color != self.color:
                    self.moves.append(x)
                    break
                else: break
            
            else: self.moves.append(x)

        #Move to right
        for i in range(1,8):

            x = self.location[0], self.location[1] + i
            if (x[0] > 7) or (x[1] > 7) or (x[0] < 0) or (x[1] < 0):
                break

            if board.get_cell(x[0], x[1]) != 0:
                if board.get_cell(x[0], x[1]).color != self.color:
                    self.moves.append(x)
                    break
                else: break
            
            else: self.moves.append(x)

        #Move to bottom
        for i in range(1,8):

            x = self.location[0] - i, self.location[1]
            if (x[0] > 7) or (x[1] > 7) or (x[0] < 0) or (x[1] < 0):
                break

            if board.get_cell(x[0], x[1]) != 0:
                if board.get_cell(x[0], x[1]).color != self.color:
                    self.moves.append(x)
                    break
                else: break
            
            else: self.moves.append(x)

        
    def __str__(self) -> str:
        return f'Rook'