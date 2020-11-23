#Anthony Persaud 500996358

import pygame
import random
WIDTH = 800 
HEIGHT = 800 
FPS = 30

n = int(input("grid size:"))
grid = [n][n]
N,S,E,W = 1,2,4,8
dx = [E==1, W==-1, N==0, S==0]
dy = [E==0, W==0, N==-1, S==1]
opp = [E==W, W==E, N==S, S==N]


def getPath(x,y,g):
    directions = [N,S,E,W]
    opp = [S,N,W,E]
    random.shuffle(directions)
    for d in directions:
        if(d=="N"):
            opp[d]=="S"
            elif(d=="S"):
                opp[d]=="N"
                elif(d=="E"):
                    opp[d]=="W"
                    elif(d=="W"):
                        opp[d]=="E"
            
        nx = x + dx[d]
        ny = y + dy[d]
        if( ((0<= ny) and (ny<=((g.length)-1)) and ((0<=nx) and (nx<=((g[ny].length)-1)) and g[ny][nx]==[0][0]):
             g[y][x].append(d)
             g[ny][nx].append(opp[d])
             getPath(nx,ny,g)
    
# initialize Pygame 
pygame.init() 
pygame.mixer.init() 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Grid") 
clock = pygame.time.Clock()

white = [255, 255, 255] 
black = [0,0,0] 
screen.fill(white) 
pygame.display.update()

running = True


while running: 
 # keep running at the at the right speed 
 clock.tick(FPS) 
 # process input (events)
 getPath(0,0,grid)

  for int i in height:
      pygame.draw.line(width * 2 - 1)
      print "|"
      for int j in width:
        if(grid[y][x] and S != 0):
            print(" ")
            else:
                pygame.draw.line()
        if (grid[y][x] !=[0][0] and E != 0):
          if((grid[y][x]!=[0][0] or grid[y][x+1]!=[0][0]) and S != 0):
              print(" ")
              else:
                  pygame.draw.line()
        else:
          print "|"
 
 
 for event in pygame.event.get(): 
 # check for closing the window 
     if (event.type == pygame.QUIT): 
         running = False
