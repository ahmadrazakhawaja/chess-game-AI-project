from board.tile import Tile
from pieces.nullpiece import nullpiece
from pieces.queen import queen
from pieces.pawn import pawn
from pieces.rook import rook
from pieces.bishop import bishop
from pieces.king import king
from pieces.knight import knight
class board:

    gameTiles = [[0 for x in range(8)] for y in range(8)]

    def __init__(self):

        pass
    def createboard(self):
        count=0
        for rows in range(8):
            for column in range(8):
                self.gameTiles[rows][column] = Tile(count,nullpiece())
                count=count+1

            self.gameTiles[0][0] = Tile(0, rook("Black", 0))
            self.gameTiles[0][1] = Tile(1, knight("Black", 1))
            self.gameTiles[0][2] = Tile(2, bishop("Black", 2))
            self.gameTiles[0][3] = Tile(3, queen("Black", 3))
            self.gameTiles[0][4] = Tile(4, king("Black", 4))
            self.gameTiles[0][5] = Tile(5, bishop("Black", 5))
            self.gameTiles[0][6] = Tile(6, knight("Black", 6))
            self.gameTiles[0][7] = Tile(7, rook("Black", 7))
            self.gameTiles[1][0] = Tile(8, pawn("Black", 8))
            self.gameTiles[1][1] = Tile(9, pawn("Black", 9))
            self.gameTiles[1][2] = Tile(10, pawn("Black", 10))
            self.gameTiles[1][3] = Tile(11, pawn("Black", 11))
            self.gameTiles[1][4] = Tile(12, pawn("Black", 12))
            self.gameTiles[1][5] = Tile(13, pawn("Black", 13))
            self.gameTiles[1][6] = Tile(14, pawn("Black", 14))
            self.gameTiles[1][7] = Tile(15, pawn("Black", 15))

            self.gameTiles[6][0] = Tile(48, pawn("White", 48))
            self.gameTiles[6][1] = Tile(49, pawn("White", 49))
            self.gameTiles[6][2] = Tile(50, pawn("White", 50))
            self.gameTiles[6][3] = Tile(51, pawn("White", 51))
            self.gameTiles[6][4] = Tile(52, pawn("White", 52))
            self.gameTiles[6][5] = Tile(53, pawn("White", 53))
            self.gameTiles[6][6] = Tile(54, pawn("White", 54))
            self.gameTiles[6][7] = Tile(55, pawn("White", 55))
            self.gameTiles[7][0] = Tile(56, rook("White", 56))
            self.gameTiles[7][1] = Tile(57, knight("White", 57))
            self.gameTiles[7][2] = Tile(58, bishop("White", 58))
            self.gameTiles[7][3] = Tile(59, queen("White", 59))
            self.gameTiles[7][4] = Tile(60, king("White", 60))
            self.gameTiles[7][5] = Tile(61, bishop("White", 61))
            self.gameTiles[7][6] = Tile(62, knight("White", 62))
            self.gameTiles[7][7] = Tile(63, rook("White", 63))

    def printboard(self):
        count = 0
        for rows in range(8):
            for column in range(8):
                print('|', end=self.gameTiles[rows][column].pieceonTile.tostring())
            print("|",end='\n')
