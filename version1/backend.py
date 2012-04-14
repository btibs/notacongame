# random swarmy stuff

import random
import math

PLAYER_STEP_SIZE = 2
ATOM_STEP_SIZE = 3

class mazemap:
	def __init__(self, width, height, hallsize):
		''' create map object '''
		self.width = width
		self.height = height
		self.hallsize = hallsize
		self.walls = []
	
	def generatewalls(self, n, len):
		'''
		generate map with n walls of average length len
		(difficulty generally increasing with each)
		'''
		
		#TODO: straight lines?
		# also lol that isn't really an average length len
		
		for i in range(0, n):
			(x1, y1) = (random.randint(0, self.width), random.randint(0, self.height))
			if random.randint(0, 1):
				(x2, y2) = (x1, random.randint(y1+len-len/10, y1+len+len/10))
			else:
				(x2, y2) = (random.randint(x1+len-len/10, x1+len+len/10), y1)
			if x2 < 0:	x2 = 0
			if y2 < 0:	y2 = 0
			self.walls.append([x1,y1,x2,y2])

class atom:
	def __init__(self, x, y):
		''' initialize '''
		self.x = x
		self.y = y
		self.step = ATOM_STEP_SIZE
	
	def randomwalk(self, xweight, yweight):
		''' move in a gaussian distribution weighted towards a particular direction '''
		self.x += random.gauss(0+xweight, 0.3*self.step)
		self.y += random.gauss(0+yweight, 0.3*self.step)
		
	def move(self):
		''' determine how to move '''
		xweight = yweight = 0
		
		# can we see the player?
		# if so, where are they?  weight +- in that direction
		
		# randomwalk!
		self.randomwalk(xweight, yweight)		
		
class walker:
	def __init__(self, x, y):
		self.step = PLAYER_STEP_SIZE
		self.x = x
		self.y = y
		
	def walk(self, x, y):
		''' move player to new location '''
		# check parent map?
		#if self.parent.map[x,y] has a wall:
		#error
		self.x = x
		self.y = y
	