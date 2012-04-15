# random swarmy stuff

import random
import math

class mazemap:
	def __init__(self, width, height, hallsize):
		''' create map object '''
		self.width = width
		self.height = height
		self.hallsize = hallsize
		self.walls = []
	
	def generateWalls(self, n, len):
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
	
	def generateBetterWalls(self, n, len):
		''' make a path of walls and something like that '''
		pass

class atom:
	def __init__(self, x, y, stepsize):
		''' initialize '''
		self.x = x
		self.y = y
		self.step = stepsize
	
	def randomwalk(self, xpoint=None, ypoint=None):
		''' move in a gaussian distribution weighted towards a particular direction
		note that this assumes self.stepsize < distance to goal point '''
		if not xpoint: xpoint = self.x
		if not ypoint: ypoint = self.y
		
		xcoeff = 1 if self.x<xpoint else -1
		ycoeff = 1 if self.y<ypoint else -1
		
		self.x += xcoeff*random.gauss(self.step, 0.5*self.step)
		self.y += ycoeff*random.gauss(self.step, 0.5*self.step)
		
		# make sure it's not hitting the walls
		if self.x < 0: self.x = 0
		if self.y < 0: self.y = 0
		
class walker:
	def __init__(self, x, y, stepsize):
		self.step = stepsize
		self.x = x
		self.y = y
		self.win = False
		
	def walk(self, x, y):
		''' move player to new location '''
		# check parent map?
		#if self.parent.map[x,y] has a wall:
		#error
		self.x = x
		self.y = y
	