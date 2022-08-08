from Model.board import Board

class GameView:

    def __init__(self) -> None:
        pass


    def get_move():
        pass


    def make_move():
        pass

    
    def display_board():
        screen_height, screen_width = 600, 600
        block_height, block_width = screen_height/8, screen_width/8
        main_display = Board(screen_height, screen_width, block_height, block_width)
        for x in range(8):
            for y in range(8):
                main_display.get_cell(x,y)
                


    def display_winner():
        pass


    def display_invalid_move():
        pass

