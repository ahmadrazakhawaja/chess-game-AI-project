from pieces.piece import piece
import math

class queen(piece):

    alliance = None
    position= None

    def __init__(self,alliance,position):
        self.alliance=alliance
        self.position=position

    def tostring(self):
        return 'Q' if self.alliance == "Black" else "q"

    def calculatecoordinates(self):
        a=self.position/8
        b=self.position%8
        return[math.floor(a),b]


    def legalmoveb(self,gametiles):
        legalmoves=[]
        x=self.calculatecoordinates()[0]
        y=self.calculatecoordinates()[1]
        a=0
        b=0
        count=0
        if(gametiles[x][y].pieceonTile.alliance=='Black'):
            while True:
                if(count==0):
                    a=x+1
                    b=y+1
                    count=count+1
                else:
                    a=a+1
                    b=b+1
                if(a<8 and b<8 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(a<8 and b<8 and gametiles[a][b].pieceonTile.alliance=='White'):
                    legalmoves.append([a,b])
                    break
                else:
                    break



            count=0
            while True:

                if(count==0):
                    a=x-1
                    b=y-1
                    count=count+1
                else:
                    a=a-1
                    b=b-1
                if(a>=0 and b>=0 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(a>=0 and b>=0 and gametiles[a][b].pieceonTile.alliance=='White'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            count=0
            while True:
                if(count==0):
                    a=x+1
                    b=y-1
                    count=count+1
                else:
                    a=a+1
                    b=b-1
                if(a<8 and b>=0 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(a<8 and b>=0 and gametiles[a][b].pieceonTile.alliance=='White'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            count=0
            while True:
                if(count==0):
                    a=x-1
                    b=y+1
                    count=count+1
                else:
                    a=a-1
                    b=b+1
                if(a>=0 and b<8 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(a>=0 and b<8 and gametiles[a][b].pieceonTile.alliance=='White'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            count=0
            while True:
                if(count==0):
                    a=x+1
                    b=y
                    count=count+1
                else:
                    a=a+1
                if(a<8 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(a<8 and gametiles[a][b].pieceonTile.alliance=='White'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            count=0
            while True:
                if(count==0):
                    a=x-1
                    b=y
                    count=count+1
                else:
                    a=a-1
                if(a>=0 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(a>=0 and gametiles[a][b].pieceonTile.alliance=='White'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            count=0
            while True:
                if(count==0):
                    a=x
                    b=y+1
                    count=count+1
                else:
                    b=b+1
                if(b<8 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(b<8 and gametiles[a][b].pieceonTile.alliance=='White'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            count=0
            while True:
                if(count==0):
                    a=x
                    b=y-1
                    count=count+1
                else:
                    b=b-1
                if(b>=0 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(b>=0 and gametiles[a][b].pieceonTile.alliance=='White'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            return legalmoves

        else:
            while True:
                if(count==0):
                    a=x+1
                    b=y+1
                    count=count+1
                else:
                    a=a+1
                    b=b+1
                if(a<8 and b<8 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(a<8 and b<8 and gametiles[a][b].pieceonTile.alliance=='Black'):
                    legalmoves.append([a,b])
                    break
                else:
                    break



            count=0
            while True:

                if(count==0):
                    a=x-1
                    b=y-1
                    count=count+1
                else:
                    a=a-1
                    b=b-1
                if(a>=0 and b>=0 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(a>=0 and b>=0 and gametiles[a][b].pieceonTile.alliance=='Black'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            count=0
            while True:
                if(count==0):
                    a=x+1
                    b=y-1
                    count=count+1
                else:
                    a=a+1
                    b=b-1
                if(a<8 and b>=0 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(a<8 and b>=0 and gametiles[a][b].pieceonTile.alliance=='Black'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            count=0
            while True:
                if(count==0):
                    a=x-1
                    b=y+1
                    count=count+1
                else:
                    a=a-1
                    b=b+1
                if(a>=0 and b<8 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(a>=0 and b<8 and gametiles[a][b].pieceonTile.alliance=='Black'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            count=0
            while True:
                if(count==0):
                    a=x+1
                    b=y
                    count=count+1
                else:
                    a=a+1
                if(a<8 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(a<8 and gametiles[a][b].pieceonTile.alliance=='Black'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            count=0
            while True:
                if(count==0):
                    a=x-1
                    b=y
                    count=count+1
                else:
                    a=a-1
                if(a>=0 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(a>=0 and gametiles[a][b].pieceonTile.alliance=='Black'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            count=0
            while True:
                if(count==0):
                    a=x
                    b=y+1
                    count=count+1
                else:
                    b=b+1
                if(b<8 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(b<8 and gametiles[a][b].pieceonTile.alliance=='Black'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            count=0
            while True:
                if(count==0):
                    a=x
                    b=y-1
                    count=count+1
                else:
                    b=b-1
                if(b>=0 and gametiles[a][b].pieceonTile.alliance is None):
                    legalmoves.append([a,b])
                    continue
                elif(b>=0 and gametiles[a][b].pieceonTile.alliance=='Black'):
                    legalmoves.append([a,b])
                    break
                else:
                    break

            return legalmoves