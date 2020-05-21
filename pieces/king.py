from pieces.piece import piece
import math

class king(piece):

    alliance = None
    position = None
    moved=False

    def __init__(self,alliance,position):
        self.alliance=alliance
        self.position=position

    def tostring(self):
        return 'K' if self.alliance == "Black" else "k"

    def calculatecoordinates(self):
        a=self.position/8
        b=self.position%8
        return[math.floor(a),b]

    def legalmoveb(self,gametiles):
        legalmoves=[]
        x=self.calculatecoordinates()[0]
        y=self.calculatecoordinates()[1]
        if(gametiles[x][y].pieceonTile.alliance=='Black'):

            if(x+1<8 and y+1<8 and not gametiles[x+1][y+1].pieceonTile.alliance=='Black'):
                legalmoves.append([x+1,y+1])

            if(x+1<8 and y-1>=0 and not gametiles[x+1][y-1].pieceonTile.alliance=='Black'):
                legalmoves.append([x+1,y-1])

            if(x+1<8 and not gametiles[x+1][y].pieceonTile.alliance=='Black'):
                legalmoves.append([x+1,y])

            if(y-1>=0 and not gametiles[x][y-1].pieceonTile.alliance=='Black'):
                legalmoves.append([x,y-1])

            if(y+1<8 and not gametiles[x][y+1].pieceonTile.alliance=='Black'):
                legalmoves.append([x,y+1])

            if(x-1>=0 and not gametiles[x-1][y].pieceonTile.alliance=='Black'):
                legalmoves.append([x-1,y])

            if(x-1>=0 and y-1>=0 and not gametiles[x-1][y-1].pieceonTile.alliance=='Black'):
                legalmoves.append([x-1,y-1])

            if(x-1>=0 and y+1<8 and not gametiles[x-1][y+1].pieceonTile.alliance=='Black'):
                legalmoves.append([x-1,y+1])

            return legalmoves

        else:
            if(x+1<8 and y+1<8 and not gametiles[x+1][y+1].pieceonTile.alliance=='White'):
                legalmoves.append([x+1,y+1])

            if(x+1<8 and y-1>=0 and not gametiles[x+1][y-1].pieceonTile.alliance=='White'):
                legalmoves.append([x+1,y-1])

            if(x+1<8 and not gametiles[x+1][y].pieceonTile.alliance=='White'):
                legalmoves.append([x+1,y])

            if(y-1>=0 and not gametiles[x][y-1].pieceonTile.alliance=='White'):
                legalmoves.append([x,y-1])

            if(y+1<8 and not gametiles[x][y+1].pieceonTile.alliance=='White'):
                legalmoves.append([x,y+1])

            if(x-1>=0 and not gametiles[x-1][y].pieceonTile.alliance=="White"):
                legalmoves.append([x-1,y])

            if(x-1>=0 and y-1>=0 and not gametiles[x-1][y-1].pieceonTile.alliance=='White'):
                legalmoves.append([x-1,y-1])

            if(x-1>=0 and y+1<8 and not gametiles[x-1][y+1].pieceonTile.alliance=='White'):
                legalmoves.append([x-1,y+1])

            return legalmoves





