import pygame
from pygame.locals import *

def back2front(gods, enemies, nahui):
	unsorted_stuff = []
	for i in gods: unsorted_stuff.append(i)
	for i in enemies:
		try:
			unsorted_stuff.append(i.horse)
			unsorted_stuff.append(i)
		except:
			unsorted_stuff.append(i)
	unsorted_stuff.append(nahui)
	sorted_stuff = sorted(unsorted_stuff, key=lambda unsorted_stuff: unsorted_stuff.rect.bottom)
	return sorted_stuff

def load_image(filename,transparency=False):
	image=pygame.image.load(filename)
	if transparency:
		image = image.convert_alpha()
	else:
		image = image.convert()
	return image

class Camera(object):
	def __init__(self, camera_func, width, height):
		self.camera_func = camera_func
		self.state = Rect(0, 0, width, height)
	
	def apply(self, target, second_layer = True):
		if second_layer == True:
			return target.rect.move(self.state.topleft)
		else:
			return target.rect.move(self.state.topleft[0]-(self.state.topleft[0]*0.75), 0)
	
	def update(self, screen, target):
		self.state = self.camera_func(self.state, target.rect)
