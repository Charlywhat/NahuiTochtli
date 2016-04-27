# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from Animate import Animate
from Animate import SFX
from Camera import load_image
	
class NahuiTochtli(pygame.sprite.Sprite):
	def __init__(self, x, y, space):
		pygame.sprite.Sprite.__init__(self)
		#SFX
		self.step = SFX(pygame.mixer.Sound("audio/sfx/nahuitochtli/step.wav"), 4)
		self.hit = SFX(pygame.mixer.Sound("audio/sfx/nahuitochtli/hit.wav"))
		self.swoosh_1 = SFX(pygame.mixer.Sound("audio/sfx/nahuitochtli/swoosh_1.wav"))
		self.swoosh_2 = SFX(pygame.mixer.Sound("audio/sfx/nahuitochtli/swoosh_2.wav"))
		self.swoosh_3 = SFX(pygame.mixer.Sound("audio/sfx/nahuitochtli/swoosh_3.wav"))
		self.swoosh_4 = SFX(pygame.mixer.Sound("audio/sfx/nahuitochtli/swoosh_4.wav"))
		
		#Sprites
		self.breathing_right = Animate([
		load_image("sprites/nahuitochtli/Nahui_right_breath_1.png", True),
		load_image("sprites/nahuitochtli/Nahui_right_breath_1.png", True),
		load_image("sprites/nahuitochtli/Nahui_right_breath_2.png", True)
		], 0.4)
		
		self.breathing_left = Animate([
		load_image("sprites/nahuitochtli/Nahui_left_breath_1.png", True),
		load_image("sprites/nahuitochtli/Nahui_left_breath_1.png", True),
		load_image("sprites/nahuitochtli/Nahui_left_breath_2.png", True)
		], 0.4)
		
		self.looking_right = Animate([
		load_image("sprites/nahuitochtli/Nahui_right_walk_1.png", True),
		load_image("sprites/nahuitochtli/Nahui_right_walk_2.png", True),
		load_image("sprites/nahuitochtli/Nahui_right_walk_3.png", True),
		], 2)
		
		self.looking_left = Animate([
		load_image("sprites/nahuitochtli/Nahui_left_walk_1.png", True),
		load_image("sprites/nahuitochtli/Nahui_left_walk_2.png", True),
		load_image("sprites/nahuitochtli/Nahui_left_walk_3.png", True),
		], 2)
		
		self.invoking = load_image("sprites/nahuitochtli/Nahui_invoke.png", True)
		self.attacking_left_1 = load_image("sprites/nahuitochtli/Nahui_left_attack_1.png", True)
		self.attacking_right_1 = load_image("sprites/nahuitochtli/Nahui_right_attack_1.png", True)
		self.attacking_left_2 = load_image("sprites/nahuitochtli/Nahui_left_attack_2.png", True)
		self.attacking_right_2 = load_image("sprites/nahuitochtli/Nahui_right_attack_2.png", True)
		self.attacking_left_3 = load_image("sprites/nahuitochtli/Nahui_left_attack_3.png", True)
		self.attacking_right_3 = load_image("sprites/nahuitochtli/Nahui_right_attack_3.png", True)
		self.attacking_left_4 = load_image("sprites/nahuitochtli/Nahui_left_attack_4.png", True)
		self.attacking_right_4 = load_image("sprites/nahuitochtli/Nahui_right_attack_4.png", True)
		self.attacking_air_right = load_image("sprites/nahuitochtli/Nahui_right_attack_air.png", True)
		self.attacking_air_left = load_image("sprites/nahuitochtli/Nahui_left_attack_air.png", True)
		
		self.jumping_right = load_image("sprites/nahuitochtli/Nahui_right_jump.png", True)
		self.jumping_left = load_image("sprites/nahuitochtli/Nahui_left_jump.png", True)
		self.covered = load_image("sprites/nahuitochtli/Nahui_cover.png", True)
		
		self.damaged = Animate([
		load_image("sprites/nahuitochtli/Nahui_damaged_1.png", True),
		load_image("sprites/nahuitochtli/Nahui_damaged_2.png", True),
		load_image("sprites/nahuitochtli/Nahui_damaged_3.png", True),
		load_image("sprites/nahuitochtli/Nahui_damaged_4.png", True),
		load_image("sprites/nahuitochtli/Nahui_damaged_5.png", True),
		load_image("sprites/nahuitochtli/Nahui_damaged_6.png", True),
		], 10)
		
		self.cover_damaged = Animate([
		load_image("sprites/nahuitochtli/Nahui_cover_damaged_1.png", True),
		load_image("sprites/nahuitochtli/Nahui_cover_damaged_2.png", True),
		], 2)
		
		self.died = load_image("sprites/nahuitochtli/Nahui_die.png", True)
		self.stunned = load_image("sprites/nahuitochtli/Nahui_die.png", True)
		
		#Position and space
		self.WIDTH = space[0]
		self.HEIGHT = space[1]
		self.image = self.breathing_right.get_current_image()
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		
		#Environment
		self.gravity = 1.3
		self.speed_x = 0.5
		self.speed_taken = 0
		self.elasticity = -0.4
		
		#Status
		self.look_left = False
		self.on_stun = False
		self.look_right = True
		self.on_invoke = False
		self.on_air = False
		self.on_attack = False
		self.on_damage = False
		self.on_cover = False
		self.on_cover_damage = False
		self.on_move = False
		self.on_breath = True
		self.ready2jump = True
		self.ready2attack = True
		self.ready2invoke = True
		self.combo_attack = 0
		
		#Attributes
		self.power = 6
		self.health = 100
		self.resistance = 0.55
	
	def move(self,time,key):
		if self.health > 0 and self.on_damage == False and self.on_cover == False and self.on_invoke == False and self.on_stun == False:
			if self.on_attack == False:
				#Up
				if self.rect.bottom>(self.HEIGHT - 70):
					if key[K_UP]:
						self.on_move = True
						if self.look_right == True:
							self.looking_right.play()
							self.image = self.looking_right.get_current_image()
						elif self.look_left == True:
							self.looking_left.play()
							self.image = self.looking_left.get_current_image()
						self.rect.centery -= self.speed_x * time
				#Down
				if self.rect.bottom<self.HEIGHT:
					if key[K_DOWN]:
						self.on_move = True
						if self.look_right == True:
							self.looking_right.play()
							self.image = self.looking_right.get_current_image()
						elif self.look_left == True:
							self.looking_left.play()
							self.image = self.looking_left.get_current_image()
						self.rect.centery += self.speed_x * time
				#Right
				if self.rect.right<self.WIDTH:
					if key[K_RIGHT]:
						self.look_left = False
						self.look_right = True
						if self.on_air == True:
							self.image = self.jumping_right
						else:
							self.on_move = True
							#Animation
							self.looking_right.play()
							self.image = self.looking_right.get_current_image()
						self.rect.centerx += self.speed_x * time
				#Left
				if self.rect.left>0:
					if key[K_LEFT]:
						self.look_left = True
						self.look_right = False
						if self.on_air == True:
							self.image = self.jumping_left
						else:
							self.on_move = True
							self.looking_left.play()
							self.image = self.looking_left.get_current_image()
						self.rect.centerx -= self.speed_x * time
				#Jump
				if self.ready2jump == True:
					if self.on_air == False:
						if key[K_SPACE]:
							self.on_air = True
							self.ready2jump = False
							if self.look_right == True:
								self.image = self.jumping_right
							elif self.look_left == True:
								self.image = self.jumping_left
							self.ground = self.rect.centery
							self.speed_taken = 0
							self.speed_y = -20
				#Cover / Invoke
				if self.on_air == False:
					if key[K_RSHIFT]:
						self.image = self.covered
						self.on_cover = True
			#Attack
			if self.ready2attack == True and self.combo_attack < 4:
				if key[K_RCTRL]:
					self.ready2attack = False
					self.on_cover = False
					if self.on_air == False:
						#Combo 1
						if self.combo_attack == 0:
							self.combo_attack = 1
							#SFX swoosh 2
							self.swoosh_2.get_sfx().play()
							if self.look_right == True:
								self.image = self.attacking_right_1
							elif self.look_left == True:
								self.image = self.attacking_left_1
						#Combo 2
						elif self.combo_attack == 1:
							self.combo_attack = 2
							if self.look_right == True:
								self.image = self.attacking_right_2
							elif self.look_left == True:
								self.image = self.attacking_left_2
						#Combo 3
						elif self.combo_attack == 2:
							self.combo_attack = 3
							if self.look_right == True:
								self.image = self.attacking_right_3
							elif self.look_left == True:
								self.image = self.attacking_left_3
						#Combo 4
						elif self.combo_attack == 3:
							self.combo_attack = 4
							self.power = 11
							#SFX swoosh 4
							self.swoosh_4.get_sfx().play()
							if self.look_right == True:
								self.image = self.attacking_right_4
							elif self.look_left == True:
								self.image = self.attacking_left_4
					else:
						#SFX swoosh
						self.swoosh_3.get_sfx().play()
						if self.look_right == True:
							self.image = self.attacking_air_right
						elif self.look_left == True:
							self.image = self.attacking_air_left
					self.attack_duration = 20
					self.on_attack = True
	
	def invoke(self, god):
		if self.ready2invoke == True:
			self.power += (god.power / 2)
			self.on_invoke = True
			self.invoke_duration = 60
			self.image = self.invoking
			self.ready2invoke = False
			
	def hitBy(self, enemy):
		if self.health > 0 and self.on_air == False and self.on_damage == False and self.on_invoke == False and self.on_stun == False and self.on_cover_damage == False:
			self.speed_y = 0
			self.damaged.play()
			if self.on_air == False:
				self.ground = self.rect.centery
			if enemy.look_right == True:
				self.look_right = True
				self.look_left = False
			if enemy.look_left == True:
				self.look_right = False
				self.look_left = True
					
			if self.on_cover == False: #Non blocked hit
				self.image = self.damaged.get_current_image()
				self.health -= enemy.power - (enemy.power * self.resistance)
				self.on_damage = True
				self.speed_taken = (enemy.power) - (enemy.power * self.resistance)
				self.speed_y = -1 * (enemy.power)
				self.on_air = True
				
			if self.on_cover == True:             #Blocked hit
				self.speed_taken = enemy.power - (enemy.power * self.resistance + 0.2)
				self.health -= (enemy.power - (enemy.power * self.resistance + 0.2))
				self.on_cover_damage = True
				self.cover_damage_duration = 30
				self.on_air = False
			
			if enemy.power - (enemy.power * self.resistance) >= 8:   #Stun hit
				self.image = self.stunned
				self.ground = self.rect.bottom - 30
				self.speed_taken = enemy.power * 2.3
				self.stun_duration = enemy.power * 10
				self.speed_taken = (enemy.power * 2) - (enemy.power * self.resistance)
				self.speed_y = -1 * (enemy.power * 2)
				self.on_damage = False
				self.on_stun = True
				self.on_air = True
			
			if self.health <= 0:             #Dead character
				self.image = self.died
				self.ground = self.rect.centery
				self.speed_taken = enemy.power * 2.3
				self.speed_y = -1 * enemy.power * 2.3
				self.on_damage = False
				self.on_air = True
		
	def update(self, rel_key):
		#Force death when health reaches 0
		if self.health <= 0:
			self.image = self.died
			self.on_attack = False
		else:
			#Breath when static
			if self.on_move == False:
				if self.on_attack == False:
					if self.on_air == False:
						if self.on_damage == False:
							if self.on_cover == False:
								if self.look_right == True:
									self.breathing_right.play()
									self.image = self.breathing_right.get_current_image()
								else:
									self.breathing_left.play()
									self.image = self.breathing_left.get_current_image()
								
				
			#Released keys
			if rel_key == K_UP or rel_key == K_DOWN or rel_key == K_RIGHT or rel_key == K_LEFT:
				self.on_move = False
			if self.health > 0:
				if rel_key == K_SPACE: self.ready2jump = True
				if rel_key == K_RCTRL: self.ready2attack = True
				if rel_key == K_RSHIFT:
					if self.on_invoke == False:
						self.on_cover = False
						if self.look_left == True:
							self.image = self.looking_left.get_current_image()
						else:
							self.image = self.looking_right.get_current_image()
			
			#On invoke
			if self.on_invoke == True:
				if self.invoke_duration > 0:
					self.invoke_duration -= 1
				else:
					#Reset values after invoke
					self.on_cover = False
					self.on_invoke = False
					if self.look_left == True:
						self.image = self.looking_left.get_current_image()
					else:
						self.image = self.looking_right.get_current_image()
					self.power = 6
					self.ready2invoke = True
					
			#On attack	
			if self.on_attack == True:
				if self.attack_duration > 0:
					self.attack_duration -= 1
				else:
					if self.look_left == True:
						self.image = self.looking_left.get_current_image()
					else:
						self.image = self.looking_right.get_current_image()
					self.combo_attack = 0
					self.power = 6
					self.on_attack = False
			#On air
			if self.on_air == True:
				if self.rect.centery + self.speed_y < self.ground:
					self.rect.centery += self.speed_y
					self.speed_y += self.gravity
					if self.look_right == True and self.rect.right < self.WIDTH:
						self.rect.centerx += self.speed_taken
					elif self.look_left == True and self.rect.left > 0:
						self.rect.centerx -= self.speed_taken
				else:
					if self.health <= 0 or self.on_stun == True:
						if self.speed_y > 11:
							self.speed_y *= self.elasticity
					else:
						if self.on_damage == True:
							self.on_damage = False
						#if self.on_cover == True:
							#self.on_cover = True
						self.rect.centery = self.ground
						self.on_air = False
						
			#On cover_damage
			if self.on_cover_damage == True:
				self.cover_damaged.play()
				if self.cover_damage_duration > 0:
					self.image = self.cover_damaged.get_current_image()
					self.cover_damage_duration -= 1
					if self.look_right == True and self.rect.right < self.WIDTH:
						self.rect.centerx += self.speed_taken
					elif self.look_left == True and self.rect.left > 0:
						self.rect.centerx -= self.speed_taken
				else:
					if self.on_cover == True:
						self.image = self.covered
					else:
						if self.look_right == True:
							self.image = self.looking_right.get_current_image()
						elif self.look_left == True:
							self.image = self.looking_left.get_current_image()
					self.on_cover_damage = False
			
			#On stun
			if self.on_stun == True:
				if self.stun_duration > 0:
					self.stun_duration -= 1
				else:
					self.ground = self.rect.top + 30
					self.on_stun = False
					if self.look_left == True:
						self.image = self.looking_left.get_current_image()
					else:
						self.image = self.looking_right.get_current_image()
				
