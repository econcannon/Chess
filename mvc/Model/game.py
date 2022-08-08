from board import Board
from player import Player

class Game:

    def __init__(self) -> None:
        self.current_player = Player.White
        self.board = Board()

    
    def check_move(self, piece):
        pass

    
    def make_move(self, location):
        self.location = location


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