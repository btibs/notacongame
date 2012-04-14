# pyglet things

import pyglet
import resources

WIDTH = 800
HEIGHT = 600

window = pyglet.window.Window(WIDTH, HEIGHT)

# make labels
bleh_label = pyglet.text.Label(text="sup", x=WIDTH/2, y=HEIGHT/2)

# make sprites
#player_sprite = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)
# etc.

player = None
atoms = [None]
game_objects = [player] + atoms

def update(dt):
	''' update the screen '''
	#for obj in game_objects:
	#	obj.update(dt)
	#for atom in atoms:
	#	atom.randomwalk()

@window.event
def on_draw():
	window.clear()
	bleh_label.draw()
	
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
	pyglet.clock.schedule_interval(update, 1/120.0)	# update at 120 Hz
	pyglet.app.run()
