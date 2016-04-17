
import pygame
from random import randint
pygame.init()
size = (500,500)
window = pygame.display.set_mode((500,500),pygame.FULLSCREEN)
pygame.display.set_caption("Pygame Bubble-Sort Visualization")
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

heightList = []
listLength = 1000
xList,y,w = [],0,1
tmpX = 0

for i in range(listLength):
    heightList.append(randint(1,500))
    xList.append(tmpX)
    tmpX += w

for i in range(listLength):
    heightList.append(i)
    xList.append(tmpX)
    tmpX += w

listLength = 2000

def draw(list_num):
    global xList,y
    for i in range(len(list_num)):
        pygame.draw.rect(window,white,(xList[i],y,w,list_num[i]),1)


def bubble_sort(alist):
    """
    Bubble Sort algorithm
    """
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        draw(alist)
        pygame.display.update()

    return alist

window.fill(black)
bubble_sort(heightList)