from bishop import Bishop
from pawn import Pawn
from rook import Rook
from queen import Queen
from king import King
from knight import Knight
#from View.game_view import GameView

import pygame


class Board:


    def __init__(self, screen_h, screen_w) -> None:
        EMPTY = int(0)
        self.screen_h = screen_h
        self.screen_w = screen_w
        self.block_h, self.block_w = screen_h/8, screen_w/8

        board = []
        board = [[EMPTY for i in range(8)] for j in range(8)]

        board[0][0] = (Rook('b', (0,0)))
        board[0][1] = Knight('b', (0,1))
        board[0][2] = Bishop('b', (0,2))
        board[0][3] = Queen('b', (0,3))
        board[0][4] = King('b', (0,4))
        board[0][5] = Bishop('b', (0,5))
        board[0][6] = Knight('b', (0,6))
        board[0][7] = Rook('b', (0,7))

        board[1][0] = Pawn('b', (1,0))
        board[1][1] = Pawn('b', (1,1))
        board[1][2] = Pawn('b', (1,2))
        board[1][3] = Pawn('b', (1,3))
        board[1][4] = Pawn('b', (1,4))
        board[1][5] = Pawn('b', (1,5))
        board[1][6] = Pawn('b', (1,6))
        board[1][7] = Pawn('b', (1,7))

        board[7][0] = Rook('b', (0,0))
        board[7][1] = Knight('b', (0,1))
        board[7][2] = Bishop('b', (0,2))
        board[7][3] = Queen('b', (0,3))
        board[7][4] = King('b', (0,4))
        board[7][5] = Bishop('b', (0,5))
        board[7][6] = Knight('b', (0,6))
        board[7][7] = Rook('b', (0,7))

        board[6][0] = Pawn('b', (1,0))
        board[6][1] = Pawn('b', (1,1))
        board[6][2] = Pawn('b', (1,2))
        board[6][3] = Pawn('b', (1,3))
        board[6][4] = Pawn('b', (1,4))
        board[6][5] = Pawn('b', (1,5))
        board[6][6] = Pawn('b', (1,6))
        board[6][7] = Pawn('b', (1,7))
        
        self.pieces_lst = []
        self.board = board

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] != 0:
                    self.pieces_lst.append(board[x][y])
        
        self.black_king_loc = (0, 4)
        self.white_king_loc = (7, 4)

        img = pygame.image.load('mvc\\Model\\Imgs\\chess_board_img.png')
        img = pygame.transform.scale(img, (self.screen_h, self.screen_w))
        self.img = img
       

    #display_board should not be in board class, should be in game_view class
    def display_board(self):
        win = pygame.display.set_mode((self.main_display.screen_h,self.main_display.screen_w))

        for x in range(8):
            for y in range(8):
                self.main_display.get_cell(x,y)
                #Check if this creates a new object each time, may be an issue (because cell of matrix contains object creation)
                piece = self.main_display.get_cell
                win.blit(self.main_display.get_cell(x,y), (self.main_display.get_cell(x,y).location[0]*self.block_w+self.block_w/4, self.main_display.get_cell(x,y).location[0]*self.block_w+self.block_w/4))


    def __str__(self):
        first = [str(x) for x in self.board[0]]
        sec = [str(x) for x in self.board[1]]
        third = [str(x) for x in self.board[2]]
        fourth = [str(x) for x in self.board[3]]
        fifth = [str(x) for x in self.board[4]]
        sixth = [str(x) for x in self.board[5]]
        seventh = [str(x) for x in self.board[6]]
        eigth = [str(x) for x in self.board[7]]
        disp_bo = [first, sec, third, fourth, fifth, sixth, seventh, eigth]

        return f'{disp_bo[0]}\n{disp_bo[1]}\n{disp_bo[2]}\n{disp_bo[3]}\n{disp_bo[4]}\n{disp_bo[5]}\n{disp_bo[6]}\n{disp_bo[7]}'


    def get_cell(self, row, col):
        return self.board[row][col]

    
    def set_cell(self, piece, row, col):
        self.board[row][col] = piece


    def get_piece_position(self, piece):
        #for piece in pieces.
        pass 
