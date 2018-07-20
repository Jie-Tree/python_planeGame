x=100
y=0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)

#create a display
import pygame
pygame.init()
screen=pygame.display.set_mode((100,100))

#wait before moving the display
import time
time.sleep(2)

#set where the display will move to
x=200
y=200
os.environ['SDL_VIDEO_WINDOW_POS']='%d,%d' %(x,y)

#resize the screen causing it to move to x y set by environ
pygame.display.set_mode((101,100))

#set the size back to normal
pygame.display.set_mode((100,100))