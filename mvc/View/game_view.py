#from Model.board import Board
import pygame
from pygame.locals import *

class GameView:

    def __init__(self, board) -> None:
        
        #self.game = game
        self.board = board
        self.screen_height, self.screen_width = 600, 600
        self.block_height, self.block_width = self.screen_height/8, self.screen_width/8

        self.window = pygame.display.set_mode((self.screen_height, self.screen_width))
        pygame.display.set_caption('Chess')
        

        #black pieces
        black_pawn_img = pygame.image.load('mvc\\Model\\Imgs\\black_pawn.png')
        black_rook_img = pygame.image.load('mvc\\Model\\Imgs\\black_rook.png')
        black_knight_img = pygame.image.load('mvc\\Model\\Imgs\\black_knight.png')
        black_bishop_img = pygame.image.load('mvc\\Model\\Imgs\\black_bishop.png')
        black_queen_img = pygame.image.load('mvc\\Model\\Imgs\\black_queen.png')
        black_king_img = pygame.image.load('mvc\\Model\\Imgs\\black_king.png')

        #white pieces
        white_pawn_img = pygame.image.load('mvc\\Model\\Imgs\\white_pawn.png')
        white_rook_img = pygame.image.load('mvc\\Model\\Imgs\\white_rook.png')
        white_knight_img = pygame.image.load('mvc\\Model\\Imgs\\white_knight.png')
        white_bishop_img = pygame.image.load('mvc\\Model\\Imgs\\white_bishop.png')
        white_queen_img = pygame.image.load('mvc\\Model\\Imgs\\white_queen.png')
        white_king_img = pygame.image.load('mvc\\Model\\Imgs\\white_king.png')

        #white piece scale
        white_pawn_img = pygame.transform.scale(white_pawn_img, (self.block_width*1/2, self.block_height*3/4))
        white_rook_img = pygame.transform.scale(white_rook_img, (self.block_width*1/2, self.block_height*3/4))
        white_knight_img = pygame.transform.scale(white_knight_img, (self.block_width*1/2, self.block_height*3/4))
        white_bishop_img = pygame.transform.scale(white_bishop_img, (self.block_width*1/2, self.block_height*3/4))
        white_queen_img = pygame.transform.scale(white_queen_img, (self.block_width*1/2, self.block_height*3/4))
        white_king_img = pygame.transform.scale(white_king_img, (self.block_width*1/2, self.block_height*3/4))

        #black piece scale
        black_pawn_img = pygame.transform.scale(black_pawn_img, (self.block_width*1/2, self.block_height*3/4))
        black_rook_img = pygame.transform.scale(black_rook_img, (self.block_width*1/2, self.block_height*3/4))
        black_knight_img = pygame.transform.scale(black_knight_img, (self.block_width*1/2, self.block_height*3/4))
        black_bishop_img = pygame.transform.scale(black_bishop_img, (self.block_width*1/2, self.block_height*3/4))
        black_queen_img = pygame.transform.scale(black_queen_img, (self.block_width*1/2, self.block_height*3/4))
        black_king_img = pygame.transform.scale(black_king_img, (self.block_width*1/2, self.block_height*3/4))

        self.b = [black_pawn_img, black_rook_img, black_knight_img, black_bishop_img, black_queen_img, black_king_img]
        self.w = [white_pawn_img, white_rook_img, white_knight_img, white_bishop_img, white_queen_img, white_king_img]

        self.x_pos, self.y_pos = self.block_width*1/4, self.block_height*1/8

        self.has_selected_piece = False
        self.has_selected_block = []
        self.display_board()
                                

    def display_board(self):
        
        self.window.blit(self.board.img, (0,0))

        blist = []
        for piece in self.board.pieces_lst:
            if piece.color == 'b':
                blist.append((piece.location, self.b[piece.img]))
            else:
                blist.append((piece.location, self.w[piece.img]))

        for pair in blist:
            self.window.blit(pair[1], (self.x_pos + pair[0][1]*self.block_width, self.y_pos + pair[0][0]*self.block_height))

        pygame.display.update()
        

    def display_winner():
        pass


    def is_selected_piece(self, piece):
 
        if not self.has_selected_piece == piece:
            self.has_selected_piece = piece
            
        else: self.has_selected_piece = False


    def is_selected_block(self, cell):

        self.has_selected_block.append(cell)
        

    def display_block_border(self):

        #if self.has_selected_block:
        #    pass
            #block here should be a location as a tuple
            #for block in self.has_selected_block:

                #Want to blit highlight of cell to indicate is selected
            #    pygame.draw.rect(self.window, (255, 0, 0), [block[0]*self.block_width, block[1]*self.block_height, self.block_height, self.block_width], 3)              
        
        p = self.has_selected_piece
        if p:

            #Want to blit highlight of cell to indicate is selected
            pygame.draw.rect(self.window, (255, 0, 0), [p.location[1]*self.block_width+1, p.location[0]*self.block_height+1, self.block_height-1, self.block_width-1], 3)

            #blits the cells for all possible moves of self.has_selected_piece
            for move in p.moves:
                pygame.draw.rect(self.window, (0, 255, 0), [move[1]*self.block_width+1, move[0]*self.block_height+1, self.block_height-1, self.block_width-1], 3)
        

    def display_invalid_move():
        pass

    
    def display_in_check(self):
        pass


    def display_current_player(self):
        pass