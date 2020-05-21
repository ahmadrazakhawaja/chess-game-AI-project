import pygame
from board.chessboard import board
import math
from pieces.nullpiece import nullpiece
from pieces.queen import queen
from pieces.rook import rook
from pieces.knight import knight
from pieces.bishop import bishop
from player.AI import AI
import copy

from board.move import move



pygame.init()
gamedisplay= pygame.display.set_mode((800,800))
pygame.display.set_caption("pychess")
clock=pygame.time.Clock()

chessBoard=board()
chessBoard.createboard()
chessBoard.printboard()
movex=move()
ai=AI()

allTiles= []
allpieces=[]

######################
######################
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('pychess', True, green, blue)
text1 = font.render('AI',True,green)
text2 = font.render('2 player',True,green)
text3=font.render('Black won by checkmate', True, green)
text4=font.render('White won by checkmate', True, green)
text5=font.render('stalemate', True, green)
text6=font.render('Made by: Ahmad Raza Khawaja', True, green)
textRect = text.get_rect()
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect5 = text5.get_rect()
textRect6 = text6.get_rect()
textRect.center = (400,100)
textRect1.center = (200,350)
textRect2.center = (600,350)
textRect3.center = (400,400)
textRect4.center = (400,400)
textRect5.center = (400,400)
textRect6.center = (400,700)





saki=''

quitgame=False

while not quitgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame= True
            pygame.quit()
            quit()

        gamedisplay.blit(text, textRect)
        pygame.draw.rect(gamedisplay,(66,134,244),[100,300,200,100])
        gamedisplay.blit(text1,textRect1)
        pygame.draw.rect(gamedisplay,(66,134,244),[500,300,200,100])
        gamedisplay.blit(text2,textRect2)
        gamedisplay.blit(text6, textRect6)

        if event.type==pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()
            if coord[0]>=100 and coord[0]<=300 and coord[1]>=300 and coord[1]<=400:
                saki='ai'
                quitgame=True
            if coord[0]>=500 and coord[0]<=700 and coord[1]>=300 and coord[1]<=400:
                saki='2 player'
                quitgame=True


        pygame.display.update()
        clock.tick(60)






def square(x,y,w,h,color):
    pygame.draw.rect(gamedisplay,color,[x,y,w,h])
    allTiles.append([color, [x,y,w,h]])

def drawchesspieces():
    xpos= 0
    ypos= 0
    color= 0
    width= 100
    height= 100
    black= (66,134,244)
    white=(143,155,175)
    number=0

    for rows in range(8):
        for column in range(8):
            if color%2==0:
                square(xpos,ypos,width,height,white)
                if not chessBoard.gameTiles[rows][column].pieceonTile.tostring() == "-":
                    img = pygame.image.load("./chessart/"
                                            + chessBoard.gameTiles[rows][column].pieceonTile.alliance[0].upper()
                                            + chessBoard.gameTiles[rows][column].pieceonTile.tostring().upper()
                                            + ".png")
                    img=pygame.transform.scale(img, (100,100))
                    allpieces.append([img,[xpos,ypos],chessBoard.gameTiles[rows][column].pieceonTile])

                xpos +=100

            else:
                square(xpos,ypos,width,height,black)
                if not chessBoard.gameTiles[rows][column].pieceonTile.tostring() == "-":
                    img = pygame.image.load("./chessart/"
                                        + chessBoard.gameTiles[rows][column].pieceonTile.alliance[0].upper()
                                        + chessBoard.gameTiles[rows][column].pieceonTile.tostring().upper()
                                        + ".png")
                    img=pygame.transform.scale(img, (100,100))
                    allpieces.append([img,[xpos,ypos],chessBoard.gameTiles[rows][column].pieceonTile])

                xpos +=100

            color +=1
            number +=1

        color +=1
        xpos=0
        ypos+=100
        for img in allpieces:
            gamedisplay.blit(img[0],img[1])

drawchesspieces()


def updateposition(x,y):
    a=x*8
    b=a+y
    return b

def givecolour(x,y):

    if y%2==0:
        if x%2==0:
            return [143,155,175]
        else:
            return [66,134,244]

    else:
        if x%2==0:
            return [66,134,244]
        else:
            return[143,155,175]




if saki=='2 player':

    moves=[]
    enpassant=[]
    promote=[]
    promotion=False
    turn=0

    array=[]
    quitgame=False

    while not quitgame:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitgame= True
                pygame.quit()
                quit()

            if movex.checkw(chessBoard.gameTiles)[0]=='checked' and len(moves)==0 :
                array=movex.movesifcheckedw(chessBoard.gameTiles)
                if len(array)==0:
                    saki='end1'
                    quitgame=True

            if movex.checkb(chessBoard.gameTiles)[0]=='checked' and len(moves)==0 :
                array=movex.movesifcheckedb(chessBoard.gameTiles)
                if len(array)==0:
                    saki='end2'
                    quitgame=True


            if movex.checkb(chessBoard.gameTiles)[0]=='notchecked' and turn%2==1 and len(moves)==0 :
                check=False
                for x in range(8):
                    for y in range(8):
                        if chessBoard.gameTiles[y][x].pieceonTile.alliance=='Black' and turn%2==1:
                            moves1=chessBoard.gameTiles[y][x].pieceonTile.legalmoveb(chessBoard.gameTiles)
                            lx1=movex.pinnedb(chessBoard.gameTiles,moves1,y,x)
                            if len(lx1)==0:
                                continue
                            else:
                                check=True
                            if check==True:
                                break
                    if check==True:
                        break


                if check==False:
                    saki='end3'
                    quitgame=True

            if movex.checkw(chessBoard.gameTiles)[0]=='notchecked' and turn%2==0 and len(moves)==0 :
                check=False
                for x in range(8):
                    for y in range(8):
                        if chessBoard.gameTiles[y][x].pieceonTile.alliance=='White' and turn%2==0:
                            moves1=chessBoard.gameTiles[y][x].pieceonTile.legalmoveb(chessBoard.gameTiles)
                            lx1=movex.pinnedw(chessBoard.gameTiles,moves1,y,x)
                            if len(lx1)==0:
                                continue
                            else:
                                check=True
                            if check==True:
                                break
                    if check==True:
                        break


                if check==False:
                    saki='end3'
                    quitgame=True

                                









            if event.type==pygame.MOUSEBUTTONDOWN:
                if movex.checkw(chessBoard.gameTiles)[0]=='checked' and len(moves)==0 :
                    array=movex.movesifcheckedw(chessBoard.gameTiles)
                    coord=pygame.mouse.get_pos()
                    m=math.floor(coord[0]/100)
                    n=math.floor(coord[1]/100)
                    imgx=pygame.transform.scale(pygame.image.load("./chessart/red_square.png",), (100,100))
                    mx=[]
                    ma=[]
                    for move in array:
                        if(move[1]==m and move[0]==n):
                            mx=[move[3]*100,move[2]*100]
                            ma=[move[2],move[3]]
                            moves.append(ma)
                            gamedisplay.blit(imgx,mx)
                            x=move[1]
                            y=move[0]
                    break

                if movex.checkb(chessBoard.gameTiles)[0]=='checked' and len(moves)==0 :
                    array=movex.movesifcheckedb(chessBoard.gameTiles)
                    coord=pygame.mouse.get_pos()
                    m=math.floor(coord[0]/100)
                    n=math.floor(coord[1]/100)
                    imgx=pygame.transform.scale(pygame.image.load("./chessart/red_square.png",), (100,100))
                    mx=[]
                    ma=[]
                    for move in array:
                        if(move[1]==m and move[0]==n):
                            mx=[move[3]*100,move[2]*100]
                            ma=[move[2],move[3]]
                            moves.append(ma)
                            gamedisplay.blit(imgx,mx)
                            x=move[1]
                            y=move[0]
                    break

                if not len(promote)==0:
                    coord = pygame.mouse.get_pos()
                    m=math.floor(coord[0]/100)
                    n=math.floor(coord[1]/100)
                    if  chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile.alliance=='Black':
                        for i in range(len(promote)):
                            if i==4:
                                turn=turn-1
                                break
                            if promote[i][0]==n and promote[i][1]==m:
                                if i==0:
                                    chessBoard.gameTiles[promote[4][1]][promote[4][0]].pieceonTile=queen('Black',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile=nullpiece()
                                    break
                                if i==1:
                                    chessBoard.gameTiles[promote[4][1]][promote[4][0]].pieceonTile=rook('Black',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile=nullpiece()
                                    break
                                if i==2:
                                    chessBoard.gameTiles[promote[4][1]][promote[4][0]].pieceonTile=knight('Black',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile=nullpiece()
                                    break
                                if i==3:
                                    chessBoard.gameTiles[promote[4][1]][promote[4][0]].pieceonTile=bishop('Black',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile=nullpiece()
                                    break

                    if  chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile.alliance=='White':
                        for i in range(len(promote)):
                            if i==4:
                                turn=turn-1
                                break
                            if promote[i][0]==n and promote[i][1]==m:
                                if i==0:
                                    chessBoard.gameTiles[promote[4][1]][promote[4][0]].pieceonTile=queen('White',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile=nullpiece()
                                    break
                                if i==1:
                                    chessBoard.gameTiles[promote[4][1]][promote[4][0]].pieceonTile=rook('White',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile=nullpiece()
                                    break
                                if i==2:
                                    chessBoard.gameTiles[promote[4][1]][promote[4][0]].pieceonTile=knight('White',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile=nullpiece()
                                    break
                                if i==3:
                                    chessBoard.gameTiles[promote[4][1]][promote[4][0]].pieceonTile=bishop('White',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile=nullpiece()
                                    break

                    allTiles.clear()
                    allpieces.clear()
                    chessBoard.printboard()
                    drawchesspieces()
                    promote=[]
                    promotion=False







                if not len(moves)==0:
                    coord = pygame.mouse.get_pos()
                    m=math.floor(coord[0]/100)
                    n=math.floor(coord[1]/100)
                    for move in moves:
                        if move[0]==n and move[1]==m:
                            turn=turn+1
                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='K' or chessBoard.gameTiles[y][x].pieceonTile.tostring()=='R' or chessBoard.gameTiles[y][x].pieceonTile.tostring()=='k' or chessBoard.gameTiles[y][x].pieceonTile.tostring()=='r':
                                chessBoard.gameTiles[y][x].pieceonTile.moved=True


                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='K' and m==x+2:
                                chessBoard.gameTiles[y][x+1].pieceonTile=chessBoard.gameTiles[y][x+3].pieceonTile
                                s=updateposition(y,x+1)
                                chessBoard.gameTiles[y][x+1].pieceonTile.position=s
                                chessBoard.gameTiles[y][x+3].pieceonTile=nullpiece()
                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='K' and m==x-2:
                                chessBoard.gameTiles[y][x-1].pieceonTile=chessBoard.gameTiles[y][0].pieceonTile
                                s=updateposition(y,x-1)
                                chessBoard.gameTiles[y][x-1].pieceonTile.position=s
                                chessBoard.gameTiles[y][0].pieceonTile=nullpiece()

                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='k' and m==x+2:
                                chessBoard.gameTiles[y][x+1].pieceonTile=chessBoard.gameTiles[y][x+3].pieceonTile
                                s=updateposition(y,x+1)
                                chessBoard.gameTiles[y][x+1].pieceonTile.position=s
                                chessBoard.gameTiles[y][x+3].pieceonTile=nullpiece()
                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='k' and m==x-2:
                                chessBoard.gameTiles[y][x-1].pieceonTile=chessBoard.gameTiles[y][0].pieceonTile
                                s=updateposition(y,x-1)
                                chessBoard.gameTiles[y][x-1].pieceonTile.position=s
                                chessBoard.gameTiles[y][0].pieceonTile=nullpiece()



                            if not len(enpassant)==0:
                                chessBoard.gameTiles[enpassant[0]][enpassant[1]].pieceonTile.enpassant=False
                                enpassant=[]
                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='P' and y+1==n and x+1==m and chessBoard.gameTiles[n][m].pieceonTile.tostring()=='-':
                                chessBoard.gameTiles[y][x+1].pieceonTile=nullpiece()
                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='P' and y+1==n and x-1==m and chessBoard.gameTiles[n][m].pieceonTile.tostring()=='-':
                                chessBoard.gameTiles[y][x-1].pieceonTile=nullpiece()

                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p' and y-1==n and x+1==m and chessBoard.gameTiles[n][m].pieceonTile.tostring()=='-':
                                chessBoard.gameTiles[y][x+1].pieceonTile=nullpiece()
                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p' and y-1==n and x-1==m and chessBoard.gameTiles[n][m].pieceonTile.tostring()=='-':
                                chessBoard.gameTiles[y][x-1].pieceonTile=nullpiece()

                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p' and n==y-2:
                                chessBoard.gameTiles[y][x].pieceonTile.enpassant=True
                                enpassant=[n,m]

                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='P' and n==y+2:
                                chessBoard.gameTiles[y][x].pieceonTile.enpassant=True
                                enpassant=[n,m]

                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='P' and y+1==n and y==6:
                                promotion=True

                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p' and y-1==n and y==1:
                                promotion=True


                            if promotion==False:

                                chessBoard.gameTiles[n][m].pieceonTile=chessBoard.gameTiles[y][x].pieceonTile
                                chessBoard.gameTiles[y][x].pieceonTile=nullpiece()
                                s=updateposition(n,m)
                                chessBoard.gameTiles[n][m].pieceonTile.position=s
                    if promotion==False:
                        allTiles.clear()
                        allpieces.clear()
                        chessBoard.printboard()
                        drawchesspieces()
                        moves=[]

                    if promotion==True:
                        if  chessBoard.gameTiles[y][x].pieceonTile.tostring()=='P' and x==7 and y==6:
                            pygame.draw.rect(gamedisplay,(255,255,255),[x*100-100,(y*100)-200,200,200])
                            imgx=pygame.transform.scale(pygame.image.load("./chessart/BQ.png",), (100,100))
                            imgx1=pygame.transform.scale(pygame.image.load("./chessart/BR.png",), (100,100))
                            imgx2=pygame.transform.scale(pygame.image.load("./chessart/BN.png",), (100,100))
                            imgx3=pygame.transform.scale(pygame.image.load("./chessart/BB.png",), (100,100))
                            gamedisplay.blit(imgx,[x*100-100,(y*100)-200])
                            gamedisplay.blit(imgx1,[(x*100),(y*100)-200])
                            gamedisplay.blit(imgx2,[x*100-100,(y*100)-100])
                            gamedisplay.blit(imgx3,[(x*100),(y*100)-100])
                            promote=[[y-2,x-1],[y-2,x],[y-1,x],[y-1,x],[m,n],[y,x]]

                        elif chessBoard.gameTiles[y][x].pieceonTile.tostring()=='P':
                            pygame.draw.rect(gamedisplay,(255,255,255),[x*100,(y*100)-200,200,200])
                            imgx=pygame.transform.scale(pygame.image.load("./chessart/BQ.png",), (100,100))
                            imgx1=pygame.transform.scale(pygame.image.load("./chessart/BR.png",), (100,100))
                            imgx2=pygame.transform.scale(pygame.image.load("./chessart/BN.png",), (100,100))
                            imgx3=pygame.transform.scale(pygame.image.load("./chessart/BB.png",), (100,100))
                            gamedisplay.blit(imgx,[x*100,(y*100)-200])
                            gamedisplay.blit(imgx1,[(x*100)+100,(y*100)-200])
                            gamedisplay.blit(imgx2,[x*100,(y*100)-100])
                            gamedisplay.blit(imgx3,[(x*100)+100,(y*100)-100])
                            promote=[[y-2,x],[y-2,x+1],[y-1,x],[y-1,x+1],[m,n],[y,x]]

                        elif  chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p' and x==7 and y==1:
                            pygame.draw.rect(gamedisplay,(0,0,0),[x*100-100,(y*100)+100,200,200])
                            imgx=pygame.transform.scale(pygame.image.load("./chessart/WQ.png",), (100,100))
                            imgx1=pygame.transform.scale(pygame.image.load("./chessart/WR.png",), (100,100))
                            imgx2=pygame.transform.scale(pygame.image.load("./chessart/WN.png",), (100,100))
                            imgx3=pygame.transform.scale(pygame.image.load("./chessart/WB.png",), (100,100))
                            gamedisplay.blit(imgx,[x*100-100,(y*100)+200])
                            gamedisplay.blit(imgx1,[(x*100),(y*100)+200])
                            gamedisplay.blit(imgx2,[x*100-100,(y*100)+100])
                            gamedisplay.blit(imgx3,[(x*100),(y*100)+100])
                            promote=[[y+2,x-1],[y+2,x],[y+1,x],[y+1,x],[m,n],[y,x]]

                        elif chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p':
                            pygame.draw.rect(gamedisplay,(0,0,0),[x*100,(y*100)+100,200,200])
                            imgx=pygame.transform.scale(pygame.image.load("./chessart/WQ.png",), (100,100))
                            imgx1=pygame.transform.scale(pygame.image.load("./chessart/WR.png",), (100,100))
                            imgx2=pygame.transform.scale(pygame.image.load("./chessart/WN.png",), (100,100))
                            imgx3=pygame.transform.scale(pygame.image.load("./chessart/WB.png",), (100,100))
                            gamedisplay.blit(imgx,[x*100,(y*100)+200])
                            gamedisplay.blit(imgx1,[(x*100)+100,(y*100)+200])
                            gamedisplay.blit(imgx2,[x*100,(y*100)+100])
                            gamedisplay.blit(imgx3,[(x*100)+100,(y*100)+100])
                            promote=[[y+2,x],[y+2,x+1],[y+1,x],[y+1,x+1],[m,n],[y,x]]










                else:
                    drawchesspieces()
                    coords = pygame.mouse.get_pos()
                    x=math.floor(coords[0]/100)
                    y=math.floor(coords[1]/100)
                    mx=[]
                    if(not chessBoard.gameTiles[y][x].pieceonTile.tostring()=='-'):
                        moves=chessBoard.gameTiles[y][x].pieceonTile.legalmoveb(chessBoard.gameTiles)
                        if(chessBoard.gameTiles[y][x].pieceonTile.tostring()=='K'):
                            ax=movex.castlingb(chessBoard.gameTiles)
                            if not len(ax)==0:
                                for l in ax:
                                    if l=='ks':
                                        moves.append([0,6])
                                    if l=='qs':
                                        moves.append([0,2])
                        if(chessBoard.gameTiles[y][x].pieceonTile.tostring()=='k'):
                            ax=movex.castlingw(chessBoard.gameTiles)
                            if not len(ax)==0:
                                for l in ax:
                                    if l=='ks':
                                        moves.append([7,6])
                                    if l=='qs':
                                        moves.append([7,2])
                        if(chessBoard.gameTiles[y][x].pieceonTile.tostring()=='P'):
                            ay=movex.enpassantb(chessBoard.gameTiles,y,x)
                            if not len(ay)==0:
                                if ay[1]=='r':
                                    moves.append([y+1,x+1])
                                else:
                                    moves.append([y+1,x-1])

                        if(chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p'):
                            ay=movex.enpassantb(chessBoard.gameTiles,y,x)
                            if not len(ay)==0:
                                if ay[1]=='r':
                                    moves.append([y-1,x+1])
                                else:
                                    moves.append([y-1,x-1])


                    if chessBoard.gameTiles[y][x].pieceonTile.alliance=='Black':
                        lx=movex.pinnedb(chessBoard.gameTiles,moves,y,x)
                    if chessBoard.gameTiles[y][x].pieceonTile.alliance=='White':
                        lx=movex.pinnedw(chessBoard.gameTiles,moves,y,x)
                    moves=lx

                    if turn%2==0:
                        if chessBoard.gameTiles[y][x].pieceonTile.alliance=='Black':
                            moves=[]
                    else:
                        if chessBoard.gameTiles[y][x].pieceonTile.alliance=='White':
                            moves=[]


                    imgx=pygame.transform.scale(pygame.image.load("./chessart/red_square.png",), (100,100))
                    for move in moves:
                        mx=[move[1]*100,move[0]*100]
                        gamedisplay.blit(imgx,mx)









        for img in allpieces:
            gamedisplay.blit(img[0],img[1])




        pygame.display.update()
        clock.tick(60)

if saki=='ai':

    moves=[]
    enpassant=[]
    promote=[]
    promotion=False
    turn=0

    array=[]
    quitgame=False

    while not quitgame:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitgame= True
                pygame.quit()
                quit()


            if movex.checkw(chessBoard.gameTiles)[0]=='checked' and len(moves)==0 :
                array=movex.movesifcheckedw(chessBoard.gameTiles)
                if len(array)==0:
                    saki='end1'
                    quitgame=True
                    break

            if movex.checkb(chessBoard.gameTiles)[0]=='checked' and len(moves)==0 :
                array=movex.movesifcheckedb(chessBoard.gameTiles)
                if len(array)==0:
                    saki='end2'
                    quitgame=True
                    break


            if movex.checkb(chessBoard.gameTiles)[0]=='notchecked' and turn%2==1 and len(moves)==0 :
                check=False
                for x in range(8):
                    for y in range(8):
                        if chessBoard.gameTiles[y][x].pieceonTile.alliance=='Black' and turn%2==1:
                            moves1=chessBoard.gameTiles[y][x].pieceonTile.legalmoveb(chessBoard.gameTiles)
                            lx1=movex.pinnedb(chessBoard.gameTiles,moves1,y,x)
                            if len(lx1)==0:
                                continue
                            else:
                                check=True
                            if check==True:
                                break
                    if check==True:
                        break


                if check==False:
                    saki='end3'
                    quitgame=True
                    break

            if movex.checkw(chessBoard.gameTiles)[0]=='notchecked' and turn%2==0 and len(moves)==0 :
                check=False
                for x in range(8):
                    for y in range(8):
                        if chessBoard.gameTiles[y][x].pieceonTile.alliance=='White' and turn%2==0:
                            moves1=chessBoard.gameTiles[y][x].pieceonTile.legalmoveb(chessBoard.gameTiles)
                            lx1=movex.pinnedw(chessBoard.gameTiles,moves1,y,x)
                            if len(lx1)==0:
                                continue
                            else:
                                check=True
                            if check==True:
                                break
                    if check==True:
                        break


                if check==False:
                    saki='end3'
                    quitgame=True





            if not turn%2==0 and promotion==False:

                turn=turn+1
                sc=copy.deepcopy(chessBoard.gameTiles)
                y,x,fx,fy=ai.evaluate(sc)
                m=fy
                n=fx
                if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='K' or chessBoard.gameTiles[y][x].pieceonTile.tostring()=='R':
                    chessBoard.gameTiles[y][x].pieceonTile.moved=True

                if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='K' and m==x+2:
                    chessBoard.gameTiles[y][x+1].pieceonTile=chessBoard.gameTiles[y][x+3].pieceonTile
                    s=updateposition(y,x+1)
                    chessBoard.gameTiles[y][x+1].pieceonTile.position=s
                    chessBoard.gameTiles[y][x+3].pieceonTile=nullpiece()
                if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='K' and m==x-2:
                    chessBoard.gameTiles[y][x-1].pieceonTile=chessBoard.gameTiles[y][0].pieceonTile
                    s=updateposition(y,x-1)
                    chessBoard.gameTiles[y][x-1].pieceonTile.position=s
                    chessBoard.gameTiles[y][0].pieceonTile=nullpiece()


                if not len(enpassant)==0:
                    chessBoard.gameTiles[enpassant[0]][enpassant[1]].pieceonTile.enpassant=False
                    enpassant=[]
                if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='P' and y+1==n and x+1==m and chessBoard.gameTiles[n][m].pieceonTile.tostring()=='-':
                    chessBoard.gameTiles[y][x+1].pieceonTile=nullpiece()
                if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='P' and y+1==n and x-1==m and chessBoard.gameTiles[n][m].pieceonTile.tostring()=='-':
                    chessBoard.gameTiles[y][x-1].pieceonTile=nullpiece()

                if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='P' and n==y+2:
                    chessBoard.gameTiles[y][x].pieceonTile.enpassant=True
                    enpassant=[n,m]

                if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='P' and y+1==n and y==6:
                    promotion=True


                if promotion==False:

                    chessBoard.gameTiles[n][m].pieceonTile=chessBoard.gameTiles[y][x].pieceonTile
                    chessBoard.gameTiles[y][x].pieceonTile=nullpiece()
                    s=updateposition(n,m)
                    chessBoard.gameTiles[n][m].pieceonTile.position=s
                    allTiles.clear()
                    allpieces.clear()
                    chessBoard.printboard()
                    drawchesspieces()
                    moves=[]

                if promotion==True:

                    if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='P':
                        chessBoard.gameTiles[y][x].pieceonTile=nullpiece()
                        chessBoard.gameTiles[n][m].pieceonTile=queen('Black',updateposition(n,m))
                        allTiles.clear()
                        allpieces.clear()
                        chessBoard.printboard()
                        drawchesspieces()
                        moves=[]
                        promote=[]
                        promotion=False






            if event.type==pygame.MOUSEBUTTONDOWN:
                if movex.checkw(chessBoard.gameTiles)[0]=='checked' and len(moves)==0 :
                    array=movex.movesifcheckedw(chessBoard.gameTiles)
                    coord=pygame.mouse.get_pos()
                    m=math.floor(coord[0]/100)
                    n=math.floor(coord[1]/100)
                    imgx=pygame.transform.scale(pygame.image.load("./chessart/red_square.png",), (100,100))
                    mx=[]
                    ma=[]
                    for move in array:
                        if(move[1]==m and move[0]==n):
                            mx=[move[3]*100,move[2]*100]
                            ma=[move[2],move[3]]
                            moves.append(ma)
                            gamedisplay.blit(imgx,mx)
                            x=move[1]
                            y=move[0]
                    break

                if not len(promote)==0:
                    coord = pygame.mouse.get_pos()
                    m=math.floor(coord[0]/100)
                    n=math.floor(coord[1]/100)
                    if  chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile.alliance=='White':
                        for i in range(len(promote)):
                            if i==4:
                                turn=turn-1
                                break
                            if promote[i][0]==n and promote[i][1]==m:
                                if i==0:
                                    chessBoard.gameTiles[promote[4][1]][promote[4][0]].pieceonTile=queen('White',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile=nullpiece()
                                    break
                                if i==1:
                                    chessBoard.gameTiles[promote[4][1]][promote[4][0]].pieceonTile=rook('White',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile=nullpiece()
                                    break
                                if i==2:
                                    chessBoard.gameTiles[promote[4][1]][promote[4][0]].pieceonTile=knight('White',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile=nullpiece()
                                    break
                                if i==3:
                                    chessBoard.gameTiles[promote[4][1]][promote[4][0]].pieceonTile=bishop('White',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameTiles[promote[5][0]][promote[5][1]].pieceonTile=nullpiece()
                                    break

                    allTiles.clear()
                    allpieces.clear()
                    chessBoard.printboard()
                    drawchesspieces()
                    promote=[]
                    promotion=False







                if not len(moves)==0:
                    coord = pygame.mouse.get_pos()
                    m=math.floor(coord[0]/100)
                    n=math.floor(coord[1]/100)
                    for move in moves:
                        if move[0]==n and move[1]==m:
                            turn=turn+1
                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='k' or chessBoard.gameTiles[y][x].pieceonTile.tostring()=='r':
                                chessBoard.gameTiles[y][x].pieceonTile.moved=True



                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='k' and m==x+2:
                                chessBoard.gameTiles[y][x+1].pieceonTile=chessBoard.gameTiles[y][x+3].pieceonTile
                                s=updateposition(y,x+1)
                                chessBoard.gameTiles[y][x+1].pieceonTile.position=s
                                chessBoard.gameTiles[y][x+3].pieceonTile=nullpiece()
                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='k' and m==x-2:
                                chessBoard.gameTiles[y][x-1].pieceonTile=chessBoard.gameTiles[y][0].pieceonTile
                                s=updateposition(y,x-1)
                                chessBoard.gameTiles[y][x-1].pieceonTile.position=s
                                chessBoard.gameTiles[y][0].pieceonTile=nullpiece()



                            if not len(enpassant)==0:
                                chessBoard.gameTiles[enpassant[0]][enpassant[1]].pieceonTile.enpassant=False
                                enpassant=[]

                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p' and y-1==n and x+1==m and chessBoard.gameTiles[n][m].pieceonTile.tostring()=='-':
                                chessBoard.gameTiles[y][x+1].pieceonTile=nullpiece()
                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p' and y-1==n and x-1==m and chessBoard.gameTiles[n][m].pieceonTile.tostring()=='-':
                                chessBoard.gameTiles[y][x-1].pieceonTile=nullpiece()

                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p' and n==y-2:
                                chessBoard.gameTiles[y][x].pieceonTile.enpassant=True
                                enpassant=[n,m]


                            if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p' and y-1==n and y==1:
                                promotion=True



                            if promotion==False:

                                chessBoard.gameTiles[n][m].pieceonTile=chessBoard.gameTiles[y][x].pieceonTile
                                chessBoard.gameTiles[y][x].pieceonTile=nullpiece()
                                s=updateposition(n,m)
                                chessBoard.gameTiles[n][m].pieceonTile.position=s
                    if promotion==False:
                        allTiles.clear()
                        allpieces.clear()
                        chessBoard.printboard()
                        drawchesspieces()
                        moves=[]

                    if promotion==True:




                        if  chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p' and x==7 and y==1:
                            pygame.draw.rect(gamedisplay,(0,0,0),[x*100-100,(y*100)+100,200,200])
                            imgx=pygame.transform.scale(pygame.image.load("./chessart/WQ.png",), (100,100))
                            imgx1=pygame.transform.scale(pygame.image.load("./chessart/WR.png",), (100,100))
                            imgx2=pygame.transform.scale(pygame.image.load("./chessart/WN.png",), (100,100))
                            imgx3=pygame.transform.scale(pygame.image.load("./chessart/WB.png",), (100,100))
                            gamedisplay.blit(imgx,[x*100-100,(y*100)+200])
                            gamedisplay.blit(imgx1,[(x*100),(y*100)+200])
                            gamedisplay.blit(imgx2,[x*100-100,(y*100)+100])
                            gamedisplay.blit(imgx3,[(x*100),(y*100)+100])
                            promote=[[y+2,x-1],[y+2,x],[y+1,x],[y+1,x],[m,n],[y,x]]

                        elif chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p':
                            pygame.draw.rect(gamedisplay,(0,0,0),[x*100,(y*100)+100,200,200])
                            imgx=pygame.transform.scale(pygame.image.load("./chessart/WQ.png",), (100,100))
                            imgx1=pygame.transform.scale(pygame.image.load("./chessart/WR.png",), (100,100))
                            imgx2=pygame.transform.scale(pygame.image.load("./chessart/WN.png",), (100,100))
                            imgx3=pygame.transform.scale(pygame.image.load("./chessart/WB.png",), (100,100))
                            gamedisplay.blit(imgx,[x*100,(y*100)+200])
                            gamedisplay.blit(imgx1,[(x*100)+100,(y*100)+200])
                            gamedisplay.blit(imgx2,[x*100,(y*100)+100])
                            gamedisplay.blit(imgx3,[(x*100)+100,(y*100)+100])
                            promote=[[y+2,x],[y+2,x+1],[y+1,x],[y+1,x+1],[m,n],[y,x]]










                else:
                    drawchesspieces()
                    coords = pygame.mouse.get_pos()
                    x=math.floor(coords[0]/100)
                    y=math.floor(coords[1]/100)
                    mx=[]
                    if(chessBoard.gameTiles[y][x].pieceonTile.alliance=='White'):
                        moves=chessBoard.gameTiles[y][x].pieceonTile.legalmoveb(chessBoard.gameTiles)
                        if(chessBoard.gameTiles[y][x].pieceonTile.tostring()=='k'):
                            ax=movex.castlingw(chessBoard.gameTiles)
                            if not len(ax)==0:
                                for l in ax:
                                    if l=='ks':
                                        moves.append([7,6])
                                    if l=='qs':
                                        moves.append([7,2])
                        if(chessBoard.gameTiles[y][x].pieceonTile.tostring()=='p'):
                            ay=movex.enpassantb(chessBoard.gameTiles,y,x)
                            if not len(ay)==0:
                                if ay[1]=='r':
                                    moves.append([y-1,x+1])
                                else:
                                    moves.append([y-1,x-1])


                    if chessBoard.gameTiles[y][x].pieceonTile.alliance=='White':
                        lx=movex.pinnedw(chessBoard.gameTiles,moves,y,x)
                    moves=lx

                    if not turn%2==0:
                        moves=[]

                    if chessBoard.gameTiles[y][x].pieceonTile.alliance=='Black':
                        moves=[]

                    if chessBoard.gameTiles[y][x].pieceonTile.tostring()=='-':
                        moves=[]


                    imgx=pygame.transform.scale(pygame.image.load("./chessart/red_square.png",), (100,100))
                    for move in moves:
                        mx=[move[1]*100,move[0]*100]
                        gamedisplay.blit(imgx,mx)









        for img in allpieces:
            gamedisplay.blit(img[0],img[1])




        pygame.display.update()
        clock.tick(60)


if saki=='end1':
    quitgame=False
    while not quitgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame= True
                pygame.quit()
                quit()

            gamedisplay.blit(text3,textRect3)


            pygame.display.update()
            clock.tick(60)

if saki=='end2':
    quitgame=False
    while not quitgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame= True
                pygame.quit()
                quit()

            gamedisplay.blit(text4,textRect4)
         #  pygame.draw.rect(gamedisplay,(66,134,244),[400,400,400,400])


            pygame.display.update()
            clock.tick(60)

if saki=='end3':
    quitgame=False
    while not quitgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame= True
                pygame.quit()
                quit()

            gamedisplay.blit(text5,textRect5)
            #  pygame.draw.rect(gamedisplay,(66,134,244),[400,400,400,400])


            pygame.display.update()
            clock.tick(60)

