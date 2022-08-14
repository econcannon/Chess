from abc import ABC, abstractmethod
import pygame

from board import Board

white = []
black = []

#Move to proper file later
pygame.display()

#black pieces
black_pawn_img = pygame.image.load('mvc\\Model\\Imgs\\black_pawn.png').convert()
black_rook_img = pygame.image.load('Imgs\\black_rook.png').convert()
black_knight_img = pygame.image.load('Imgs\\black_knight.png').convert()
black_bishop_img = pygame.image.load('Imgs\\black_bishop.png').convert()
black_queen_img = pygame.image.load('Imgs\\black_queen.png').convert()
black_king_img = pygame.image.load('Imgs\\black_king.png').convert()

#white pieces
white_pawn_img = pygame.image.load('Imgs\\white_pawn.png').convert()
white_rook_img = pygame.image.load('Imgs\\white_rook.png').convert()
white_knight_img = pygame.image.load('Imgs\\white_knight.png').convert()
white_bishop_img = pygame.image.load('Imgs\\white_bishop.png').convert()
white_queen_img = pygame.image.load('Imgs\\white_queen.png').convert()
white_king_img = pygame.image.load('Imgs\\white_king.png').convert()


white = [white_pawn_img, white_rook_img, white_knight_img, white_bishop_img, white_queen_img, white_king_img]
black = [black_pawn_img, black_rook_img, black_knight_img, black_bishop_img, black_queen_img, black_king_img]

block_w, block_h = 600/8, 600/8

for img in white:
    pygame.transform.scale(img, (block_w*1/2, block_h*3/4))
for img in black:
    pygame.transform.scale(img, (block_w*1/2, block_h*3/4))




class Pieces(ABC):

    def __init__(self, color, location):
        self.color = color
        self.location = location
        self.draw
        self.moves = []
        
#for objects of certain color in pieces, check moves if move overlaps king position, king in check
    def valid_move(self, board):
        for move in self.moves:

            #check border of board
            if (move[0] < 0) or (move[1]) < 0:
                self.moves.remove(move)
            elif (move[0] > 8) or (move[1] > 8):
                self.moves.remove(move)
            
            #check if cell contains piece of own color
            if board.get_cell(move[0][1]).color == self.color:
                self.moves.remove(move)


    def update_location(self, location):
        self.location[0], self.location[1] = location[0], location[1]


    def draw_img(self, win):
        if self.color == 'b':
            img = black[self.img]
        elif self.color == 'w':
            img = white[self.img]

        x, y = self.location[0]*1/4, self.location[1]*1/8
        win.blit(img, (x,y))