#PlatformPlanet (C)2008 by Robin Wellner
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#Released under GPL (see http://www.gnu.org/licenses/)

try:
    import psyco
    psyco.full()
except:
    pass
import pygame
from pygame.locals import *
import os
from sys import platform as sys_platform
if sys_platform[:3] == 'win':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
from math import *
import random
try: import cPickle
except: import Pickle as cPickle
pygame.init()
import graphics
from clock import ABClock
