from mvc.Model.board import Board
from mvc.Model.game import Game
from mvc.View.game_view import GameView
import pygame

class GameController:

    def __init__(self) -> None:
        self.board = Board(600, 600)
        self.view = GameView(self.board)
        self.game = Game(self.board, self.view)

        
    def start_game(self):

        while not self.game.check_mate():

            #Not yet defined
            self.view.display_current_player()
            self.view.display_board()

            while True:

                cell = self.game.choose_move()
                if not self.game.check_move(self.view.has_selected_piece, cell):
                    continue

                cell_val = self.board.get_cell(cell[0], cell[1])

                if cell_val == 0:
                    had_piece = False
                else: had_piece = True

                self.game.save_temp(cell_val, self.view.has_selected_piece.location)
                #updates board info
                self.game.execute_move(self.view.has_selected_piece, cell)
                #updates list info
                self.view.board.update_list()
                #updates attribute info
                self.game.update_piece_location(cell)
                self.game.get_new_moves()

                if not self.game.is_in_check():
                    self.view.has_selected_piece = False           
                    self.view.display_board()
                    self.game.change_curr_player()
                    break

                else: 

                    if not had_piece:
                        self.game.reverse_move(piece = self.view.has_selected_piece, location = self.game.temp_pos, move = cell)
                    #1st arg is piece that was just moved
                    #2nd arg is piece that was captured
                    #3rd arg is position of piece from arg 1
                    #4th arg is position of captured piece
                    else: self.game.reverse_move(self.view.has_selected_piece, self.game.temp_piece, self.game.temp_pos, cell)

                    self.view.board.update_list()
                    self.view.display_in_check()
                    self.view.has_selected_piece = False
                    continue

                
        winner = self.model.get_winner()
        self.view.display_winner(winner)