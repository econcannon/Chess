from board import Board
from player import Player

class Game:

    def __init__(self) -> None:
        self.current_player = Player.White
        self.board = Board()
        self.turn = 0

    
    def check_move(self, piece, move):
        if move in piece.moves:
            self.execute_move(move)

    
    def choose_move(self, location):
        self.location = location


    def execute_move(self, move):
        pass
        


    def change_curr_player(self):
        if self.current_player == Player.White:
            self.current_player = Player.Black
        else: self.current_player = Player.White


    def is_in_check():
        pass


    def check_mate():
        pass


    def get_winner():
        pass