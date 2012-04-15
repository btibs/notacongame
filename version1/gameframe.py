# this file runs the game

import pyglet
from pyglet.window import key, mouse

import resources
from backend import atom, walker, mazemap

from gameparams import *

import random

def generateCritters(num, cx, cy, spread=1):
	''' generate critters in a Gaussian distribution around center of map '''
	
	# flat random version
	#critters = [atom(random.randint(WIDTH/2-WIDTH/10, WIDTH/2+WIDTH/10), random.randint(HEIGHT/2-HEIGHT/10, HEIGHT/2+HEIGHT/10)) for i in range(0, CRITTER_NUM)]
	
	critters = []
	for i in range(0, num):
		x = random.gauss(cx, CRITTER_STEP_SIZE*spread)
		y = random.gauss(cy, CRITTER_STEP_SIZE*spread)
		critters.append(atom(x,y,CRITTER_STEP_SIZE))
	
	return critters


# BEGIN MAIN PROGRAM

# set us up the window
window = pyglet.window.Window(WIDTH, HEIGHT)
keys = key.KeyStateHandler()
window.push_handlers(keys)
window.set_caption("MAZE GAME")

# make labels
bleh_label = pyglet.text.Label(text="sup", x=WIDTH/2, y=HEIGHT/2)
winlabel = pyglet.text.Label(text="YOU WIN YAY", x=WIDTH/2, y=HEIGHT/2)

# make sprites
#player_sprite = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)
# etc.

# set us up the game board
gamemap = mazemap(WIDTH, HEIGHT, HALL_SIZE)
gamemap.generateWalls(WALL_NUM, WALL_LEN)
player = walker(PLAYER_START_X, PLAYER_START_Y, PLAYER_STEP_SIZE)
critters = generateCritters(CRITTER_NUM, WIDTH/2, HEIGHT/2, 1.5)

# Event handlers

def update(dt):
	''' update the screen '''
	#for obj in game_objects:
	#	obj.update(dt)
	
	if keys[key.LEFT]:
		if not wallInTheWay('L'):
			player.x -= PLAYER_STEP_SIZE
		if player.x < 0: player.x = 0
	if keys[key.RIGHT]:
		if not wallInTheWay('R'):
			player.x += PLAYER_STEP_SIZE
		if player.x > WIDTH-PLAYER_SIZE: player.x = WIDTH-PLAYER_SIZE
	if keys[key.DOWN]:
		if not wallInTheWay('D'):
			player.y -= PLAYER_STEP_SIZE
		if player.y < 0: player.y = 0
	if keys[key.UP]:
		if not wallInTheWay('U'):
			player.y += PLAYER_STEP_SIZE
		if player.y > HEIGHT-PLAYER_SIZE: player.y = HEIGHT-PLAYER_SIZE
	
	for c in critters:
		c.randomwalk(player.x, player.y)	# no weighting, no dt?
	
	# check if you win
	if player.x >= WIDTH-PLAYER_SIZE and player.y >= HEIGHT-PLAYER_SIZE:
		player.win = True

def wallInTheWay(dir):
	''' check if there is a wall in the way '''
	x,y = (0,0)
	if dir == 'L':
		x = player.x - PLAYER_STEP_SIZE
		y = player.y
	elif dir == 'R':
		x = player.x + PLAYER_STEP_SIZE
		y = player.y
	elif dir == 'D':
		x = player.x
		y = player.y - PLAYER_STEP_SIZE
	elif dir == 'U':
		x = player.x
		y = player.y + PLAYER_STEP_SIZE
	
	for wall in gamemap.walls:
		# check each edge for a collision
		#TODO: derrrrp
		if (
			#abs(wall[0]-player.x) <= PLAYER_SIZE or
			#abs(wall[2]-player.x) <= PLAYER_SIZE or
			abs(wall[0]-x) <= PLAYER_SIZE or
			abs(wall[2]-x) <= PLAYER_SIZE
		) and (
			#abs(wall[1]-player.y) <= PLAYER_SIZE or
			#abs(wall[3]-player.y) <= PLAYER_SIZE or
			abs(wall[1]-y) <= PLAYER_SIZE or
			abs(wall[3]-y) <= PLAYER_SIZE
		):
			print "hit x: %s, %s, %s, %s" % (player.x, x, wall[0], wall[2])
			print "or maybe y %s, %s, %s, %s" % (player.y, y, wall[1], wall[3])
			return True
	
	return False
		
@window.event
def on_draw():
	window.clear()
	bleh_label.draw()
	if player.win:	winlabel.draw()
	
	# draw the player
	#pyglet.graphics.draw(PLAYER_SIZE, pyglet.gl.GL_POINTS, ('v2i', (player.x, player.y)))
	pyglet.gl.glColor4f(*COLORS['green'])
	pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (player.x, player.y,
	player.x, player.y+PLAYER_SIZE,
	player.x+PLAYER_SIZE, player.y+PLAYER_SIZE,
	player.x+PLAYER_SIZE, player.y
	)))

	# draw the critters
	pyglet.gl.glColor4f(*COLORS['aqua'])
	for c in critters:
		pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2i', (int(c.x), int(c.y))))

	# draw the walls
	pyglet.gl.glColor4f(*COLORS['white'])
	for wall in gamemap.walls:
		pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (wall[0], wall[1], wall[2], wall[3]))) #TODO this is dumb y u no unpack
	
	# draw the goal
	pyglet.gl.glColor4f(*COLORS['red'])
	pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2i', (WIDTH, HEIGHT,
	WIDTH, HEIGHT-PLAYER_SIZE,
	WIDTH-PLAYER_SIZE, HEIGHT-PLAYER_SIZE,
	WIDTH-PLAYER_SIZE, HEIGHT
	)))
		
@window.event
def on_mouse_press(x, y, button, modifiers):
	if button == mouse.LEFT:
		print "you pressed the left button"
	print "mouse pressed at point (%s, %s)"%(x, y)


if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1/UPDATE_FREQ)
	pyglet.app.run()
