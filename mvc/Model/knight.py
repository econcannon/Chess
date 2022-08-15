from pieces import Pieces

class Knight(Pieces):

    def __init__(self, color, location) -> None:
        super().__init__(color, location)
        self.img = 2
    
    def append_moves(self, board):
        x = []
        x.append((self.location[0] + 2, self.location[1] + 1))
        x.append((self.location[0] + 1, self.location[1]  + 2))
        x.append((self.location[0] + 2, self.location[1] - 1))
        x.append((self.location[0] + 1, self.location[1] - 2))
        x.append((self.location[0] - 2, self.location[1] + 1))
        x.append((self.location[0] - 1, self.location[1]  + 2))
        x.append((self.location[0] - 2, self.location[1] - 1))
        x.append((self.location[0] - 1, self.location[1] - 2))

        for pos in x:
            if board.get_cell(pos[0], pos[1]) != 0:
                
                if board.get_cell(pos[0], pos[1]).color == self.color:
                    continue
                else: self.moves.append(pos)

            else: self.moves.append(pos)
        

        
    def __str__(self) -> str:
        return f'Knight'
            

