# resource stuff

import pyglet

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

#player_image = pyglet.resource.image("player.png")
# etc

def center_image(image):
	image.anchor_x = image.width/2
	image.anchor_y = image.height/2