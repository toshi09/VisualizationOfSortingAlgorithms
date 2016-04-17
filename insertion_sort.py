import pygame
import random

from random import randint
#  import winsound #Remove if on Linux
pygame.init()
size = (500,500)
window = pygame.display.set_mode((500,500),pygame.FULLSCREEN)

pygame.display.set_caption(" Insertion-Sort Visualization")
black = pygame.Color(0,0,0)
white = pygame.Color(255,225,245)

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
        pygame.draw.rect(window,white,(xList[i],y,w,list_num[i]),0)

def insertion_sort(alist):
    """
    Insertion sort
    """
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
            alist[position]=currentvalue

        draw(alist)
        pygame.display.update()

    return alist



window.fill(black)

insertion_sort(heightList)   