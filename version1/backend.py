# random swarmy stuff

import random
import math

PLAYER_STEP_SIZE = 2
ATOM_STEP_SIZE = 3

class atom:
	def __init__(self, parent, x, y):
		''' initialize '''
		self.x = x
		self.y = y
		self.step = ATOM_STEP_SIZE
		self.parent = parent
	
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
		
class player:
	def __init__(self, parent, x, y):
		self.step = PLAYER_STEP_SIZE
		self.x = x
		self.y = y
		self.parent = parent
		
	def walk(self, x, y):
		''' move player to new location '''
		# check parent map?
		#if self.parent.map[x,y] has a wall:
		#error
		self.x = x
		self.y = y
		
class frame:
	def __init__(self, atoms, player):
		'''
		initialize the framework
		atoms is an array of atoms
		player is a player object
		'''
		self.atoms = atoms
		self.player = player
		self.generatewalls()
	
	def generatewalls(self):
		''' generate a random maze map '''
		self.map = None	# actually this should be an array of something or maybe this just draws directly
		pass # maybe there's an algorithm online?  erase lines from a grid?  with a random walk?
		