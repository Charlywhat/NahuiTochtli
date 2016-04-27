import pygame
from pygame.locals import *
from Camera import load_image
from Animate import Animate

class Codex(pygame.sprite.Sprite):
	def __init__(self):
		self.image = load_image("bg/hud/codex_a.png", True)
		self.flame = Animate([
		load_image("bg/hud/flame_1.png", True),
		load_image("bg/hud/flame_2.png", True),
		load_image("bg/hud/flame_3.png", True),
		load_image("bg/hud/flame_4.png", True),
		load_image("bg/hud/flame_5.png", True),
		load_image("bg/hud/flame_6.png", True),
		], 2)
		
		self.rect = self.image.get_rect()
		self.rect.top = 10
		self.flame.rect = self.flame.get_current_image().get_rect()
		self.health = 100
		self.fuel = 0.02
	
	def update(self):
		if self.health > 0:
			self.health -= self.fuel
