# this file runs the game

import pyglet
from pyglet.window import key, mouse

import resources
from backend import atom, walker, mazemap

from gameparams import *

import random

# BEGIN MAIN PROGRAM

# set us up the window
window = pyglet.window.Window(WIDTH, HEIGHT)
window.set_caption("MAZE GAME")

# make labels
bleh_label = pyglet.text.Label(text="sup", x=WIDTH/2, y=HEIGHT/2)

# make sprites
#player_sprite = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)
# etc.

# set us up the game board
gamemap = mazemap(WIDTH, HEIGHT, HALL_SIZE)
gamemap.generatewalls(WALL_NUM, WALL_LEN)
player = walker(0, 0)
critters = [atom(random.randint(WIDTH/2-WIDTH/10, WIDTH/2+WIDTH/10), random.randint(HEIGHT/2-HEIGHT/10, HEIGHT/2+HEIGHT/10)) for i in range(0, CRITTER_NUM)]

# Event handlers

def update(dt):
	''' update the screen '''
	#for obj in game_objects:
	#	obj.update(dt)
	for c in critters:
		c.randomwalk(0,0)	# no weighting, no dt?

@window.event
def on_draw():
	window.clear()
	bleh_label.draw()

	# draw the player
	#pyglet.graphics.draw(PLAYER_SIZE, pyglet.gl.GL_POINTS, ('v2i', (player.x, player.y)))
	pyglet.gl.glColor4f(*COLORS['green'])
	pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2i', (player.x, player.y)))

	# draw the critters
	pyglet.gl.glColor4f(*COLORS['aqua'])
	for c in critters:
		pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2i', (c.x, c.y)))

	# draw the walls
	pyglet.gl.glColor4f(*COLORS['white'])
	for wall in gamemap.walls:
		pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (wall[0], wall[1], wall[2], wall[3]))) #TODO this is dumb y u no unpack
	
@window.event
def on_key_press(symbol, modifiers):
	if symbol == key.ENTER:
		print "ENTER was pressed"
		
@window.event
def on_mouse_press(x, y, button, modifiers):
	if button == mouse.LEFT:
		print "you pressed the left button"
	print "mouse pressed at point (%s, %s)"%(x, y)


if __name__ == '__main__':
	#pyglet.clock.schedule_interval(update, 1/120.0)	# update at 120 Hz
	pyglet.app.run()
