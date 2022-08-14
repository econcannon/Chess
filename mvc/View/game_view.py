from Model.board import Board
import pygame

class GameView:

    def __init__(self) -> None:
        screen_height, screen_width = 600, 600
        block_height, block_width = screen_height/8, screen_width/8
        self.main_display = Board(screen_height, screen_width, block_height, block_width)
        self.main_display.display_board()
        pygame.display.set_caption('Chess')


    def get_move():
        pass


    def make_move():
        pass

    
    def display_board(self):
        self.main_display.display_board(self)




    def display_winner():
        pass


    def display_invalid_move():
        pass

