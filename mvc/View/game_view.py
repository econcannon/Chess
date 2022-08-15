from Model.board import Board
import pygame

class GameView:

    def __init__(self) -> None:
        self.window = pygame.display.set_mode((self.screen_height, self.screen_width))
        pygame.display.set_caption('Chess')
        screen_height, screen_width = 600, 600
        block_height, block_width = screen_height/8, screen_width/8

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
        white_pawn_img = pygame.transform.scale(white_pawn_img, (block_width*1/2, block_height*3/4))
        white_rook_img = pygame.transform.scale(white_rook_img, (block_width*1/2, block_height*3/4))
        white_knight_img = pygame.transform.scale(white_knight_img, (block_width*1/2, block_height*3/4))
        white_bishop_img = pygame.transform.scale(white_bishop_img, (block_width*1/2, block_height*3/4))
        white_queen_img = pygame.transform.scale(white_queen_img, (block_width*1/2, block_height*3/4))
        white_king_img = pygame.transform.scale(white_king_img, (block_width*1/2, block_height*3/4))

        #black piece scale
        black_pawn_img = pygame.transform.scale(black_pawn_img, (block_width*1/2, block_height*3/4))
        black_rook_img = pygame.transform.scale(black_rook_img, (block_width*1/2, block_height*3/4))
        black_knight_img = pygame.transform.scale(black_knight_img, (block_width*1/2, block_height*3/4))
        black_bishop_img = pygame.transform.scale(black_bishop_img, (block_width*1/2, block_height*3/4))
        black_queen_img = pygame.transform.scale(black_queen_img, (block_width*1/2, block_height*3/4))
        black_king_img = pygame.transform.scale(black_king_img, (block_width*1/2, block_height*3/4))

        b = [black_pawn_img, black_rook_img, black_knight_img, black_bishop_img, black_queen_img, black_king_img]
        w = [white_pawn_img, white_rook_img, white_knight_img, white_bishop_img, white_queen_img, white_king_img]

        x_pos, y_pos = block_width*1/4, block_height*1/8
        

    def get_move():
        pass


    def make_move():
        pass

    
    def display_board(self, board):
        
        self.window.blit(board.img, (0,0))

        blist = []
        for piece in board.pieces_lst:
            if piece.color == 'b':
                (self.x_pos + self.block_width, self.y_pos + self.block_height)
                blist.append((piece.location, self.b[piece.img]))
            else:
                blist.append((piece.location, self.w[piece.img]))

        for pair in blist:
            self.window.blit(pair[1], (self.x_pos + pair[0][0]*self.block_width, self.y_pos + pair[0][1]*self.block_height))
        

    def display_winner():
        pass


    def display_invalid_move():
        pass

