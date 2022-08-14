from pieces import Pieces

class King(Pieces):

    def __init__(self, color, location) -> None:
        super().__init__(self, color, location)
        self.img = 5
    
    def append_moves(self):
        #need to figure out how to check border conditions
        
        if self.color == 'w':
            #move up
            x = self.location[0] - 1, self.location[1]
            self.moves.append(x)
            #move up right 
            x = self.location[0] + 1, self.location[1] + 1
            self.moves.append(x)
            #move up left
            x = self.location[0] + 1, self.location[1] - 1
            self.moves.append(x)
            #move right
            x = self.location[0], self.location[1] + 1
            self.moves.append(x)
            #move left
            x = self.location[0], self.location[1] - 1
            self.moves.append(x)
            #move down
            x = self.location[0] - 1, self.location[1]
            self.moves.append(x)
            #move down right
            x = self.location[0] - 1, self.location[1] + 1
            self.moves.append(x)
            #move down left
            x = self.location[0] - 1, self.location[1] - 1
            self.moves.append(x)
        
        #black king moves:
        else: 
            #move up
            x = self.location[0] + 1, self.location[1]
            self.moves.append(x)
            #move up right 
            x = self.location[0] - 1, self.location[1] - 1
            self.moves.append(x)
            #move up left
            x = self.location[0] - 1, self.location[1] + 1
            self.moves.append(x)
            #move right
            x = self.location[0], self.location[1] - 1
            self.moves.append(x)
            #move left
            x = self.location[0], self.location[1] + 1
            self.moves.append(x)
            #move down
            x = self.location[0] + 1, self.location[1]
            self.moves.append(x)
            #move down right
            x = self.location[0] + 1, self.location[1] - 1
            self.moves.append(x)
            #move down left
            x = self.location[0] + 1, self.location[1] + 1
            self.moves.append(x)
