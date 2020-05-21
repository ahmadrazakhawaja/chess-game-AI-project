from pieces.nullpiece import nullpiece


class move:

    def __init__(self):
        pass

    def checkb(self,gametiles):
        x=0
        y=0
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonTile.tostring()=='K'):
                    x=m
                    y=k
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonTile.alliance=='White'):
                    moves=gametiles[m][k].pieceonTile.legalmoveb(gametiles)
                    for move in moves:
                        if(move[0]==x and move[1]==y):
                            return["checked",[m,k]]
        return["notchecked"]

    def updateposition(self,x,y):
        a=x*8
        b=a+y
        return b

    def movesifcheckedb(self,gametiles):
        movi=[]
        piece=None
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonTile.alliance=='Black'):
                    moves=gametiles[m][k].pieceonTile.legalmoveb(gametiles)
                    for move in moves:
                        x=move[0]
                        y=move[1]
                        piece=gametiles[x][y].pieceonTile
                        gametiles[x][y].pieceonTile=gametiles[m][k].pieceonTile
                        gametiles[m][k].pieceonTile=nullpiece()
                        s=self.updateposition(x,y)
                        gametiles[x][y].pieceonTile.position=s
                        if(self.checkb(gametiles)[0]=='notchecked'):
                            movi.append([m,k,x,y])
                            gametiles[m][k].pieceonTile=gametiles[x][y].pieceonTile
                            gametiles[x][y].pieceonTile=piece
                            s=self.updateposition(m,k)
                            gametiles[m][k].pieceonTile.position=s
                        else:
                            gametiles[m][k].pieceonTile=gametiles[x][y].pieceonTile
                            gametiles[x][y].pieceonTile=piece
                            s=self.updateposition(m,k)
                            gametiles[m][k].pieceonTile.position=s


        return movi

    def checkw(self,gametiles):
        x=0
        y=0
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonTile.tostring()=='k'):
                    x=m
                    y=k
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonTile.alliance=='Black'):
                    moves=gametiles[m][k].pieceonTile.legalmoveb(gametiles)
                    if moves==None:
                        print(m)
                        print(k)
                    for move in moves:
                        if(move[0]==x and move[1]==y):
                            return["checked",[m,k]]
        return["notchecked"]

    def movesifcheckedw(self,gametiles):
        movi=[]
        piece=None
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonTile.alliance=='White'):
                    moves=gametiles[m][k].pieceonTile.legalmoveb(gametiles)
                    for move in moves:
                        x=move[0]
                        y=move[1]
                        piece=gametiles[x][y].pieceonTile
                        gametiles[x][y].pieceonTile=gametiles[m][k].pieceonTile
                        gametiles[m][k].pieceonTile=nullpiece()
                        s=self.updateposition(x,y)
                        gametiles[x][y].pieceonTile.position=s
                        if(self.checkw(gametiles)[0]=='notchecked'):
                            movi.append([m,k,x,y])
                            gametiles[m][k].pieceonTile=gametiles[x][y].pieceonTile
                            gametiles[x][y].pieceonTile=piece
                            s=self.updateposition(m,k)
                            gametiles[m][k].pieceonTile.position=s
                        else:
                            gametiles[m][k].pieceonTile=gametiles[x][y].pieceonTile
                            gametiles[x][y].pieceonTile=piece
                            s=self.updateposition(m,k)
                            gametiles[m][k].pieceonTile.position=s


        return movi

    def castlingb(self,gametiles):
        array=[]
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonTile.tostring()=='K'):
                    if(gametiles[m][k].pieceonTile.moved==False):
                        if(gametiles[m][k+3].pieceonTile.tostring()=='R'):
                            if(gametiles[m][k+3].pieceonTile.moved==False):
                                if(gametiles[m][k+1].pieceonTile.tostring()=='-'):
                                    if(gametiles[m][k+2].pieceonTile.tostring()=='-'):
                                        array.append('ks')
                        if(gametiles[m][0].pieceonTile.tostring()=='R'):
                            if(gametiles[m][0].pieceonTile.moved==False):
                                if(gametiles[m][3].pieceonTile.tostring()=='-'):
                                    if(gametiles[m][2].pieceonTile.tostring()=='-'):
                                        if(gametiles[m][1].pieceonTile.tostring()=='-'):
                                            array.append('qs')
                    return array
    def castlingw(self,gametiles):
        array=[]
        for m in range(8):
            for k in range(8):
                if(gametiles[m][k].pieceonTile.tostring()=='k'):
                    if(gametiles[m][k].pieceonTile.moved==False):
                        if(gametiles[m][k+3].pieceonTile.tostring()=='r'):
                            if(gametiles[m][k+3].pieceonTile.moved==False):
                                if(gametiles[m][k+1].pieceonTile.tostring()=='-'):
                                    if(gametiles[m][k+2].pieceonTile.tostring()=='-'):
                                        array.append('ks')
                        if(gametiles[m][0].pieceonTile.tostring()=='r'):
                            if(gametiles[m][0].pieceonTile.moved==False):
                                if(gametiles[m][3].pieceonTile.tostring()=='-'):
                                    if(gametiles[m][2].pieceonTile.tostring()=='-'):
                                        if(gametiles[m][1].pieceonTile.tostring()=='-'):
                                            array.append('qs')
                    return array



    def enpassantb(self,gametiles,y,x):

        if(gametiles[y][x].pieceonTile.tostring()=='P' and y==4):
            if(x+1<8 and gametiles[y][x+1].pieceonTile.tostring()=='p' and gametiles[y][x+1].pieceonTile.enpassant==True):
                return[[y,x],'r']
            if(x-1>=0 and gametiles[y][x-1].pieceonTile.tostring()=='p' and gametiles[y][x-1].pieceonTile.enpassant==True):
                return[[y,x],'l']

        if(gametiles[y][x].pieceonTile.tostring()=='p' and y==3):
            if(x+1<8 and gametiles[y][x+1].pieceonTile.tostring()=='P' and gametiles[y][x+1].pieceonTile.enpassant==True):
                return[[y,x],'r']
            if(x-1>=0 and gametiles[y][x-1].pieceonTile.tostring()=='P' and gametiles[y][x-1].pieceonTile.enpassant==True):
                return[[y,x],'l']

        return []


    def pinnedb(self,gametiles,moves,y,x):
        movi=[]
        piece1=None
        for move in moves:
            m=move[0]
            k=move[1]
            piece1=gametiles[m][k].pieceonTile
            gametiles[m][k].pieceonTile=gametiles[y][x].pieceonTile
            gametiles[y][x].pieceonTile=nullpiece()
            if(self.checkb(gametiles)[0]=='notchecked'):
                movi.append(move)
            gametiles[y][x].pieceonTile=gametiles[m][k].pieceonTile
            gametiles[m][k].pieceonTile=piece1

        return movi

    def pinnedw(self,gametiles,moves,y,x):
        movi=[]
        piece1=None
        for move in moves:
            m=move[0]
            k=move[1]
            piece1=gametiles[m][k].pieceonTile
            gametiles[m][k].pieceonTile=gametiles[y][x].pieceonTile
            gametiles[y][x].pieceonTile=nullpiece()
            if(self.checkw(gametiles)[0]=='notchecked'):
                movi.append(move)
            gametiles[y][x].pieceonTile=gametiles[m][k].pieceonTile
            gametiles[m][k].pieceonTile=piece1

        return movi























































