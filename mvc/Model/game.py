from board import Board
from player import Player
from king import King

class Game:
    EMPTY = int(0)

    def __init__(self, board = 0) -> None:
        self.current_player = Player.White
        if board:
            self.board = board
        else: self.board = Board(600, 600)
        self.turn = 0

    
    def move_conglom(self):

        while True:

            location, piece = self.choose_move()
            if self.check_move(piece, location):
                self.execute_move(piece, location)
                if piece == 'King':
                    if piece.color == 'b':
                        self.board.black_king_loc = location
                    else: self.board_white_loc = location
                break
            else: continue

        #at end of execute:
        self.change_curr_player()
        

    def check_move(self, piece, move):
        if move in piece.moves:
            return True
        else: return False

    
    def choose_move(self, location):
        self.location = location


    def execute_move(self, piece, location):
        if self.board.get_cell(location[0], location[1]) != 0:
            self.remove_piece(location)

        r = piece.location
        self.remove_piece(r)
        self.board.set_cell(piece, location[0], location[1])


    def remove_piece(self, location):
        self.board.board[location[0]][location[1]] = self.EMPTY


    def change_curr_player(self):
        if self.current_player == Player.White:
            self.current_player = Player.Black
        else: self.current_player = Player.White


    def is_in_check(self):
        black_king_loc = 0#fill in the king position
        white_king_loc = 0#fill in the king position

        for piece in self.board.pieces_lst:
            if piece.color == 'w':
                if black_king_loc in piece.moves:
                    return True
                else: continue
            if piece.color == 'b':
                if white_king_loc in piece.moves:
                    return True
                else: continue
        return False
                


    def check_mate():
        pass


    def get_winner():
        pass