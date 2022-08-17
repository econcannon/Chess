from mvc.Model.player import Player
from mvc.View.game_view import GameView
from mvc.Model.board import Board
import pygame
from pygame.locals import *

class Game:
    EMPTY = int(0)

    def __init__(self, board: Board, view: GameView) -> None:

        self.view = view
        self.current_player = Player.White
        self.other_player = Player.Black
        self.board = board
        self.turn = 0
        self.temp_piece = 0
        self.temp_pos = (0, 0)
        
    
    def get_new_moves(self):
        
            #Deletes prior move possibilities
            for piece in self.board.pieces_lst:
                piece.moves = []
                #Finds moves based on new position
                piece.append_moves(self.board)


    def check_move(self, piece, move):

        piece.append_moves(self.board)
        if move in piece.moves:

            return True
        else: return False

    
    def choose_move(self):

        #Returns the position of cell selected

        while True:
            
            pygame.display.update()
            #pygame.time.delay(10)
            mx, my = pygame.mouse.get_pos()
            row, col = int(my/self.view.block_height), int(mx/self.view.block_width)
                        
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
        
                    if event.button == 1:
                        pos = (row, col)
                        cell = self.board.get_cell(pos[0], pos[1])

                        if cell == 0:
                            if self.view.has_selected_piece:
                                return pos
                            #else do nothing, because, no reason to select empty cell without selected piece

                        else: 
                            if cell.color == self.current_player:

                                if self.view.has_selected_piece:
                                    cell.append_moves(self.board)
                                    self.view.display_board()
                                    self.view.is_selected_piece(cell)
                                    self.view.display_block_border()
                                    pygame.display.update()
                                    continue

                                else: 
                                    self.view.is_selected_piece(cell)
                                    self.view.display_block_border()
                                    pygame.display.update()

                            else:
                                if self.view.has_selected_piece:
                                    return pos
                        
                                #else do nothing, because, no reason to select opponent piece without selected piece  
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 


    def execute_move(self, piece, location):

        if self.board.get_cell(location[0], location[1]) != 0:
            captured = self.board.get_cell(location[0], location[1])
            self.capture_piece(captured)

        cell = piece.location
        self.remove_piece(cell)
        self.board.set_cell(piece, location[0], location[1])
        piece.turn += 1


    def save_temp(self, piece, location):

        self.temp_pos = location
        self.temp_piece = piece


    def reverse_move(self, piece, location, other = 0, move = 0):
        if other:
            #self then:
            #1st arg is piece that was just moved
            #2nd arg is piece that was captured
            #3rd arg is position of piece from arg 1 before movement
            #4th arg is position of captured piece
            piece.turn -= 1
            #restores location attribute
            piece.location = location
            #restores moved piece
            self.board.set_cell(piece, location[0], location[1])
            self.remove_piece(location)
            #restores captured piece
            self.board.set_cell(other, move[0], move[1])
            #restores list 
            self.board.pieces_lst.append(other)
            piece.append_moves(self.board)
            self.view.display_board()

        else: 
            piece.turn -= 1
            #restore attribute
            piece.location = location
            #restore board
            self.board.set_cell(piece, location[0], location[1])
            self.remove_piece(move)
            piece.append_moves(self.board)
            self.view.display_board()


    def remove_piece(self, location):

        self.board.board[location[0]][location[1]] = self.EMPTY


    def capture_piece(self, piece):

        self.remove_piece(piece.location)
        self.board.pieces_lst.remove(piece)


    def change_curr_player(self):

        if self.current_player == Player.White:
            self.current_player = Player.Black
            self.other_player = Player.White
        else: 
            self.current_player = Player.White
            self.other_player = Player.Black


    def is_in_check(self):

        black_king_loc = self.board.black_king_pos
        white_king_loc = self.board.white_king_pos

        #append each pieces moves to ensure updated
        for piece in self.board.pieces_lst:

            piece.append_moves(self.board)

        #once all moves are appended, see if in check
        for piece in self.board.pieces_lst:

            if self.current_player == 'w':

                if piece.color == 'w':
                    continue

                if piece.color == 'b':

                    if white_king_loc in piece.moves:
                        return True
                    else: continue
            
            else:

                if piece.color == 'w':
            
                    if black_king_loc in piece.moves:
                        return True
                    else: continue

                if piece.color == 'b':
                    continue

        return False
                

    def check_mate(self):
        return False


    def get_winner():
        pass


    def update_piece_location(self, location):

        self.view.has_selected_piece.location = location