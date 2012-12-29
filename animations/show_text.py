from acabsl import WALLSIZEX,WALLSIZEY,update,send
import time
import string
from sys import stdin
import pygame

WALL = 1
FPS = 10
# lines to be put above and below the font. 
# for the current setup, a value of -1 works best, 
# because pygame renders fonts too small
PADDING = -1
# font is from http://04.jp.org/
FONT_FILENAME = 'data/04B_24.TTF'
COLOR = (255,255,255)
# currently only used in the padding areas
BGCOLOR = (0,0,0)
# time [s] that a frame is updatet
SCREEN_DURATION = (FPS**-1)
# time [s] for fading in/out each pixel
FADE_TIME = 0.01#SCREEN_DURATION
# string of characters the font can display
# others are omitted
CHARSET = string.digits+string.letters+string.punctuation+' '

def get_dotmatrix(string):
	''' returns a list of vertical lines, which are lists of (r,g,b)-triplets '''
	f = pygame.font.Font(FONT_FILENAME,(WALLSIZEY - 2*PADDING))
	scrawl = f.render(string,False,COLOR)
	width = scrawl.get_width()
	height = scrawl.get_height()
	# blank screen at the beginning
	dotmatrix = [[BGCOLOR]*WALLSIZEY]*WALLSIZEX
	# and the middle, w/ padding pixels above and below
	dotmatrix.extend([([BGCOLOR]*PADDING + 
		[scrawl.get_at((x,y))[0:3] for y in range(height)] + 
		[BGCOLOR]*PADDING) for x in range(width)])
	# blank screen at the end
	dotmatrix.extend([[BGCOLOR]*(height + PADDING)]*WALLSIZEX)
	return dotmatrix

def scrowl(matrix):
	'''Generator to create a scrolling cutout from the matrix'''
	# this coud be optimized, but, meh.
	for offset in range(len(matrix)):
		yield matrix[offset:offset+WALLSIZEX]

def update_screen(columns):
	'''send the columns to the leds'''
	for x,col in enumerate(columns):
		for y,color in enumerate(col):
			r,g,b = color
			send(WALL,x,y,r,g,b,FADE_TIME)
	update()

def get_lines(fp):
	'''yields a line from fp whenever it's ready
the 'ugly' characters, such as umlauts are thrown away.'''
	line = fp.readline()
	while(line!=''):
		line = line.expandtabs(4)
		yield ''.join([c for c in line if c in CHARSET])
		line = fp.readline()

if __name__ == '__main__':
	pygame.init()
	update()
	for line in get_lines(stdin):
		for screen in scrowl(get_dotmatrix(line)):
			update_screen(screen)
			time.sleep(SCREEN_DURATION)	
