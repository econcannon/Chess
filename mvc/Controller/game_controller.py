from Model.game import Game
from View.game_view import GameView

class GameController:

    def __init__(self, model: Game, view: GameView) -> None:
        self.model: model
        self.view = view
        

    def start_game(self):
        while not self.model.check_mate():
            self.view.display_board()

            piece, row, col = self.view.get_move()
            while not self.model.check_move(piece, row, col):
                self.view.display_invalid_move()
                piece, row, col = self.view.get_move()

            self.view.make_move(piece, row, col)
            self.model.change_curr_player()

        winner = self.model.get_winner()
        self.view.display_winner(winner)
        

