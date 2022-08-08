from bishop import Bishop
from pawn import Pawn
from rook import Rook
from queen import Queen
from king import King
from knight import Knight
import pygame

class Board:


    def __init__(self, screen_h, screen_w, block_h, block_w) -> None:
        board = [
            [[Rook('b', (0,0))],[Knight('b', (0,1))],[Bishop('b', (0,2))],[Queen('b', (0,3))],[King('b', (0,4))],[Bishop('b', (0,5))],[Knight('b', (0,6))],[Rook('b', (0,7))]],
            [[Pawn('b', (1,0))],[Pawn('b', (1,1))],[Pawn('b', (1,2))],[Pawn('b', (1,3))],[Pawn('b', (1,4))],[Pawn('b', (1,5))],[Pawn('b', (1,6))],[Pawn('b', (1,7))]],
            [[''],[''],[''],[''],[''],[''],[''],['']],
            [[''],[''],[''],[''],[''],[''],[''],['']],
            [[''],[''],[''],[''],[''],[''],[''],['']],
            [[''],[''],[''],[''],[''],[''],[''],['']],
            [[Pawn('w', (6,0))],[Pawn('w', (6,1))],[Pawn('w', (6,2))],[Pawn('w', (6,3))],[Pawn('w', (6,4))],[Pawn('w', (6,5))],[Pawn('w', (6,6))],[Pawn('w', (6,7))]],
            [[Rook('w', (7,0))],[Knight('w', (7,1))],[Bishop('w', (7,2))],[Queen('w', (7,3))],[King('w', (7,4))],[Bishop('w', (7,5))],[Knight('w', (7,6))],[Rook('w', (7,7))]],
        ]
        
        self.screen_h = screen_h
        self.screen_w = screen_w
        self.block_h = block_h
        self.block_w = block_w
        self.board = board
        img = pygame.image.load('Imgs\\chess_board_img.png')
        img = pygame.trasnform.scale(self.screen_h, self.screen_w)
        self.img = img


    def display_board(self):
        print(f'{self.board[0]}\n{self.board[1]}\n{self.board[2]}\n{self.board[3]}\n{self.board[4]}\n{self.board[5]}\n{self.board[6]}\n{self.board[7]}')


    def __str__(self):
        f'{self.board[0]}\n{self.board[1]}\n{self.board[2]}\n{self.board[3]}\n{self.board[4]}\n{self.board[5]}\n{self.board[6]}\n{self.board[7]}'


    def get_cell(self, row, col):
        return self.board[row][col]

    
    def set_cell(self, row, col, piece):
        pass