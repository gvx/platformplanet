import pygame
from math import pi

def aacircle_old(Surface,color,pos,radius,resolution,width=0): #new aacircle() is probably faster
    for I in xrange(resolution):
        pygame.draw.aaline(Surface, color, (pos[0] + radius*cos(2*pi*float(I)/resolution), pos[1] + radius*sin(2*pi*float(I)/resolution)), (pos[0] + radius*cos(2*pi*float(I+1)/resolution), pos[1] + radius*sin(2*pi*float(I+1)/resolution)))

def aacircle(Surface,color,pos,radius,resolution,width=0):
    q = 2*pi/resolution
    points = [(pos[0] + radius*cos(q*I), pos[1] + radius*sin(q*I)) for I in xrange(resolution)]
    pygame.draw.aalines(Surface, color, True, points)