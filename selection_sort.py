
import random

from random import randint
pygame.init()
size = (500,500)
window = pygame.display.set_mode((500,500),pygame.FULLSCREEN)
pygame.display.set_caption("Pygame Bubble-Sort Visualization")
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

heightList = []
listLength = 2000
xList,y,w = [],0,1
tmpX = 0

for i in range(listLength):
    heightList.append(randint(1,500))
    xList.append(tmpX)
    tmpX += w


def draw(list_num):
    global xList,y
    for i in range(len(list_num)):
        pygame.draw.rect(window,white,(xList[i],y,w,list_num[i]),0)

def selection_sort(alist):
    """
    Selection sort
    """
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

        draw(alist)
        pygame.display.update()

    return alist 

window.fill(black)
selection_sort(heightList)   