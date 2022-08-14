from pieces import Pieces
from board import Board
import Model.Imgs 

class Bishop(Pieces):

    def __init__(self, color, location) -> None:
        super().__init__(self, color, location)
        self.img = 3


    def append_moves(self, board):
        i = 0
        subset = []


        #up to the right
        i = 0
        while self.location[0] < 8 and self.location[1] < 8:

            if self.color == 'w':
                #up to the right for white
                x = self.location[0] + i, self.location[1] + i

            else: 
                #up to the right for black
                x = self.location[0] - i, self.location[1] - i

            if board.get_cell(x[0], x[1]) != 0:
                if board.get_cell(x[0],x[1]).color == self.color:
                    break
                if board.get_cell(x[0],x[1]).color != self.color:
                    self.moves.append(x)
                    break

            self.moves.append(x)
            




        #up to the left
        i = 0
        while self.location[0] < 8 and self.location[1] < 8:

            if self.color == 'w':
                #up to the left for white
                y = self.location[0] + i, self.location[1] - i
                subset.append(y)
            else:
                #up to the left for black
                y = self.location[0] - i, self.location[1] + i
                subset.append(y)
        

        #down to the left
        i = 0
        while self.location[0] < 8 and self.location[1] < 8:

            if self.color == 'w':
                #down to the left for white
                k = self.location[0] - i, self.location[1] - i
                subset.append(k)
            else:
                #down to the left for black
                k = self.location[0] + i, self.location[1] + i
                subset.append(k)
        

        #down to the right
        i = 0
        while self.location[0] < 8 and self.location[1] < 8:

            if self.color == 'w':
                #down to the right for white
                j = self.location[0] - i, self.location[1] + i
                subset.append(j)
            else:
                #down to the right for black
                j = self.location[0] + i, self.location[1] - i
                subset.append(j)
            
        for move in subset:
            if board.get_cell(move[0], move[1]) == 0:
                self.moves.append(move)
            else: break
        i += 1            


    def move_piece(self):
        pass


    def __str__(self):
        f'bishop'