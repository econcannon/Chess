import pieceClasses 
from pieceClasses.pawn import Pawn
from pieceClasses.queen import Queen
from pieceClasses.king import King
from pieceClasses.rook import Rook
from pieceClasses.knight import Knight
from pieceClasses.bishop import Bishop


class Pieces:


    def __init__(self, role, color, rank):
        role_dict = {'pawn': Pawn(color, rank),
                     'rook': Rook(color, rank),
                     'knight': Knight(color, rank),
                     'bishop': Bishop(color, rank),
                     'king': King(color, rank),
                     'queen': Queen(color, rank)}

        if not role in role_dict:
            raise IOError('Invalid role')
        role_dict['pawn']
        #create dict of current pieces on board


    def valid_move(self, rank, color):
        #for objects of certain color in pieces, check moves if move overlaps king position, king in check
        pass


