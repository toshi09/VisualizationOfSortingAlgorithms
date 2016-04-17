#Python 2.7 Bubble-Sort Visualization By Lucid Potato
import pygame
from random import randint
#  import winsound #Remove if on Linux
pygame.init()

#screen = pygame.display.get_surface()
#wid,hit = screen.get_width(),screen.get_height()
#flags = screen.get_flags()

window = pygame.display.set_mode((500,500),pygame.FULLSCREEN)
pygame.display.set_caption("Pygame Merge-Sort Visualization")
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
    global xList,y
    for i in range(len(list_num)):
        pygame.draw.rect(window,white,(xList[i],y,w,list_num[i]),0)


def merge(left, right):
    """
    Merge two sorted lists.
    Used by merge_sort algorithm.
    """
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

def merge_sort(m):
    """
    Merge Sort Algorithm
    """
 
    if len(m) <= 1:
        return m
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)

    merged_list = merge(left, right)

    draw(merged_list)
    pygame.display.update()
    return merged_list


window.fill(black)

result = merge_sort(heightList)