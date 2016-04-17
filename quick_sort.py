import pygame
import random

from random import randint
pygame.init()
size = (500,500)
window = pygame.display.set_mode((500,500),pygame.FULLSCREEN)
pygame.display.set_caption(" QuickSort-Sort Visualization")
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

def draw(list_num):
    global xList,y, window
    for i in range(len(list_num)):
        pygame.draw.rect(window,white,(xList[i],0 ,w,list_num[i]),0)


def compare(a,b):
    """
    Compare two numbers
    """
    if a<b: return (-1)
    if a>b: return( 1)
    return( 0)

def distribute(bins,L,fn):
    """
    helper routine for quick sort.
    """
    for item in L:
        bins[fn(item)].append(item)

def qsort(L):
    """
    QuickSort algorithm
    """
    if len(L)<2: return L
    pivot_element = random.choice(L)
    bins = {-1:[],0:[],1:[]}
    distribute(bins,L, lambda item : compare(item, pivot_element) )
    sorted_list = qsort(bins[-1])+bins[0]+qsort(bins[1])
    draw(sorted_list)
    pygame.display.update()
    return sorted_list


window.fill(black)

qsort(heightList)