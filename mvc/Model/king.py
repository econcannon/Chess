from pieces import Pieces

class King(Pieces):

    def __init__(self, color, location) -> None:
        super().__init__(color, location)
        self.img = 5
    

    def append_moves(self, board):
        #need to figure out how to check border conditions
        x = []

        x.append(self.location[0] - 1, self.location[1])                        
        x.append(self.location[0] + 1, self.location[1] + 1)            
        x.append(self.location[0] + 1, self.location[1] - 1)                        
        x.append(self.location[0], self.location[1] + 1)            
        x.append(self.location[0], self.location[1] - 1)
        x.append(self.location[0] - 1, self.location[1])
        x.append(self.location[0] - 1, self.location[1] + 1)
        x.append(self.location[0] - 1, self.location[1] - 1)

        for pos in x:
            if (pos[0] > 8) or (pos[1] > 8) or (pos[0] < 0) or pos[1] < 0:
                x.remove(pos)
            cell = board.get_cell(pos[0], pos[1])
            
            if cell != 0:
                if cell.color == self.color:
                    x.remove(pos)

            self.moves.append(pos)



        

    def __str__(self) -> str:
        return f'King'