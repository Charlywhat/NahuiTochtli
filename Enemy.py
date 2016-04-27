# -*- coding: utf-8 -*-
import pygame
import Pose
from pygame.locals import *
from Gods import *
from Animate import Animate
from Animate import SFX
from Camera import load_image

class Horse(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		#Position and space
		self.image = self.looking_right.get_current_image()
		self.rect = self.image.get_rect()
		
		#Status
		self.look_left = True
		self.look_right = False
		self.on_ride = True
		
		#Attributes
		self.health = 500
		self.speed_x = 0.28
	
	def update(self, rider):
		if self.on_ride:
			if self.health <= 0:
				#Lay down if health reaches zero
				self.on_ride = False
			
			else:
				#Follow rider
				self.rect.centery = rider.rect.centery + 2
				self.look_left = rider.look_left
				self.look_right = rider.look_right
				#STUNNED ANIMATION
				if rider.on_stun:
					self.stunned.play()
					self.image = self.stunned.get_current_image()
				#DOING NOTHING
				elif rider.doing_nothing:
					self.layed.play()
					self.image = self.layed.get_current_image()
				#RUNNING ANIMATION
				elif self.look_right:
					self.looking_right.play()
					self.image = self.looking_right.get_current_image()
					self.rect.centerx = rider.rect.centerx
				elif self.look_left:
					self.looking_left.play()
					self.image = self.looking_left.get_current_image()
					self.rect.centerx = rider.rect.centerx
						
		else:
			self.layed.play()
			self.image = self.layed.get_current_image()
			#LAY DOWN ANIMATION

class Horse1(Horse):
	def __init__(self):
		#Sprites
		self.looking_right = Animate([
		load_image("sprites/spanish/horse1/right_run_1.png", True),
		load_image("sprites/spanish/horse1/right_run_2.png", True),
		load_image("sprites/spanish/horse1/right_run_3.png", True),
		load_image("sprites/spanish/horse1/right_run_4.png", True),
		load_image("sprites/spanish/horse1/right_run_5.png", True),
		load_image("sprites/spanish/horse1/right_run_6.png", True),
		load_image("sprites/spanish/horse1/right_run_7.png", True),
		load_image("sprites/spanish/horse1/right_run_8.png", True),
		], 3.5)
		
		self.looking_left = Animate([
		load_image("sprites/spanish/horse1/left_run_1.png", True),
		load_image("sprites/spanish/horse1/left_run_2.png", True),
		load_image("sprites/spanish/horse1/left_run_3.png", True),
		load_image("sprites/spanish/horse1/left_run_4.png", True),
		load_image("sprites/spanish/horse1/left_run_5.png", True),
		load_image("sprites/spanish/horse1/left_run_6.png", True),
		load_image("sprites/spanish/horse1/left_run_7.png", True),
		load_image("sprites/spanish/horse1/left_run_8.png", True),
		], 3.5)
		
		self.stunned = Animate([
		load_image("sprites/spanish/horse1/stun_4.png", True),
		load_image("sprites/spanish/horse1/stun_5.png", True),
		load_image("sprites/spanish/horse1/stun_6.png", True),
		], 2)
		
		self.layed = Animate([
		load_image("sprites/spanish/horse1/layed_1.png", True),
		load_image("sprites/spanish/horse1/layed_2.png", True),
		load_image("sprites/spanish/horse1/layed_3.png", True),
		load_image("sprites/spanish/horse1/layed_4.png", True),
		load_image("sprites/spanish/horse1/layed_5.png", True),
		load_image("sprites/spanish/horse1/layed_6.png", True),
		], 1)
		super(Horse1, self).__init__()
	
	def update(self, rider):
		super(Horse1, self).update(rider)

class Horse2(Horse):
	def __init__(self):
		#Sprites
		self.looking_right = Animate([
		load_image("sprites/spanish/horse2/right_run_1.png", True),
		load_image("sprites/spanish/horse2/right_run_2.png", True),
		load_image("sprites/spanish/horse2/right_run_3.png", True),
		load_image("sprites/spanish/horse2/right_run_4.png", True),
		load_image("sprites/spanish/horse2/right_run_5.png", True),
		load_image("sprites/spanish/horse2/right_run_6.png", True),
		load_image("sprites/spanish/horse2/right_run_7.png", True),
		load_image("sprites/spanish/horse2/right_run_8.png", True),
		], 3.5)
		
		self.looking_left = Animate([
		load_image("sprites/spanish/horse2/left_run_1.png", True),
		load_image("sprites/spanish/horse2/left_run_2.png", True),
		load_image("sprites/spanish/horse2/left_run_3.png", True),
		load_image("sprites/spanish/horse2/left_run_4.png", True),
		load_image("sprites/spanish/horse2/left_run_5.png", True),
		load_image("sprites/spanish/horse2/left_run_6.png", True),
		load_image("sprites/spanish/horse2/left_run_7.png", True),
		load_image("sprites/spanish/horse2/left_run_8.png", True),
		], 3.5)
		
		self.stunned = Animate([
		load_image("sprites/spanish/horse2/stun_4.png", True),
		load_image("sprites/spanish/horse2/stun_5.png", True),
		load_image("sprites/spanish/horse2/stun_6.png", True),
		], 2)
		
		self.layed = Animate([
		load_image("sprites/spanish/horse2/layed_1.png", True),
		load_image("sprites/spanish/horse2/layed_2.png", True),
		load_image("sprites/spanish/horse2/layed_3.png", True),
		load_image("sprites/spanish/horse2/layed_4.png", True),
		load_image("sprites/spanish/horse2/layed_5.png", True),
		load_image("sprites/spanish/horse2/layed_6.png", True),
		], 1)
		super(Horse2, self).__init__()
	
	def update(self, rider):
		super(Horse2, self).update(rider)
	
		
	
class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y, space, pose = "coward"):
		pygame.sprite.Sprite.__init__(self)
		
		#Position and space
		self.WIDTH = space[0]
		self.HEIGHT = space[1]
		self.image = self.breathing_left.get_current_image()
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		
		#Status
		self.look_left = True
		self.look_right = False
		self.doing_nothing = False
		self.on_locked = False
		self.on_air = False
		self.on_stun = False
		self.on_attack = False
		self.on_damage = False
		self.on_cover = False 
		self.ready2attack = True
		
		#Environment
		self.gravity = 1.5
		self.speed_x = 0.09
		self.speed_taken = 0
		self.elasticity = -0.4
		
		#Attributes
		self.pose = pose
		self.reload_time = 0
		self.sword_power = 5
		self.rifle_power = 10
		self.power = 0
		self.health = 100
		self.resistance = 0.25
		self.rifle_range = 400 #Actual range: From 230 to rifle_range
		
	def ai(self, target, time):
		#Force death when health reaches 0
		if self.health <= 0:
			self.image = self.died
		
		#Do nothing when target is dead
		if (target.health <= 0 or target.on_stun == True) and self.health > 0 and self.on_damage == False and self.on_attack == False and self.on_stun == False:
			self.doing_nothing = True
			if self.look_right:
				self.breathing_right.play()
				self.image = self.breathing_right.get_current_image()
			else:
				self.breathing_left.play()
				self.image = self.breathing_left.get_current_image()
		#Move	
		elif self.health > 0 and self.on_damage == False and self.on_cover == False and self.on_attack == False and self.on_stun == False and target.on_stun == False:
			self.doing_nothing = False
			if (self.rect.centerx < target.rect.centerx and target.look_left == True) or (self.rect.centerx > target.rect.centerx and target.look_right == True):
				self.on_locked = True
			else: self.on_locked = False
			in_advantage = abs(self.rect.centerx - target.rect.centerx) > 230
			#Make decition
			if self.pose == "crafty":
				decition = Pose.crafty([self.on_locked, target.on_attack, target.on_cover, target.on_air, in_advantage])
			elif self.pose == "coward":
				decition = Pose.coward([self.on_locked, target.on_attack, target.on_cover, target.on_air, in_advantage])
			elif self.pose == "aggressive":
				decition = Pose.aggressive([self.on_locked, target.on_attack, target.on_cover, target.on_air, in_advantage])
			if decition == 1:
				#Reach target
				#Up
				if self.rect.bottom>(self.HEIGHT - 70):
					if self.rect.centery > target.rect.centery:
						if self.look_right:
							self.looking_right.play()
							self.image = self.looking_right.get_current_image()
						elif self.look_left:
							self.looking_left.play()
							self.image = self.looking_left.get_current_image()
						self.rect.centery -= self.speed_x * time
				#Down
				if self.rect.bottom<self.HEIGHT:
					if self.rect.centery < target.rect.centery:
						if self.look_right:
							self.looking_right.play()
							self.image = self.looking_right.get_current_image()
						elif self.look_left:
							self.looking_left.play()
							self.image = self.looking_left.get_current_image()
						self.rect.centery += self.speed_x * time
				#Right
				if self.rect.right<self.WIDTH:
					if target.rect.centerx>self.rect.centerx:
						self.look_left = False
						self.look_right = True
						self.looking_right.play()
						self.image = self.looking_right.get_current_image()
						self.rect.centerx += self.speed_x * time
				#Left
				if self.rect.left>0:
					if target.rect.centerx<self.rect.centerx:
						self.look_left = True
						self.look_right = False
						self.looking_left.play()
						self.image = self.looking_left.get_current_image()
						self.rect.centerx -= self.speed_x * time
				#Attack
				if target.health > 0:
					if self.ready2attack:
						#Close
						if abs(self.rect.centerx - target.rect.centerx) < 80:
							self.power = self.sword_power
							self.swoosh.get_sfx().play()
							if self.look_right:
								self.image = self.attacking_right
							else:
								self.image = self.attacking_left
							self.on_cover = False
							self.attack_duration = 10
							self.ready2attack = False
							self.reload_time = 30
							self.on_attack = True
								
						#Far
						if abs(self.rect.centerx - target.rect.centerx) < self.rifle_range:
							if abs(self.rect.centerx - target.rect.centerx) > 230:
								self.power = self.rifle_power + (-1 * (abs(int(self.rect.centerx - target.rect.centerx)/100)))
								self.shot.get_sfx().play()
								if target.rect.centerx > self.rect.centerx:
									self.look_right = True
									self.look_left = False
									self.image = self.attacking_right_far
								else:
									self.look_right = False
									self.look_left = True
									self.image = self.attacking_left_far
								self.on_cover = False
								self.attack_duration = 30
								self.ready2attack = False
								self.reload_time = 70
								self.on_attack = True
				
								
			elif decition == -1:
				#Retreat
				if target.health > 0:
					#Attack when in range
					if self.ready2attack == True and (abs(self.rect.centerx - target.rect.centerx) < self.rifle_range and abs(self.rect.centerx - target.rect.centerx) > 230):
						self.power = self.rifle_power + (-1 * (abs(int(self.rect.centerx - target.rect.centerx)/100)))
						self.shot.get_sfx().play()
						if target.rect.centerx > self.rect.centerx:
							self.look_right = True
							self.look_left = False
							self.image = self.attacking_right_far
						else:
							self.look_right = False
							self.look_left = True
							self.image = self.attacking_left_far
						self.on_cover = False
						self.attack_duration = 10
						self.ready2attack = False
						self.reload_time = 70
						self.on_attack = True
					#Close attack
					elif self.ready2attack == True and abs(self.rect.centerx - target.rect.centerx) < 30:
						self.power = self.sword_power
						self.swoosh.get_sfx().play()
						if self.look_right:
							self.image = self.attacking_right
						else:
							self.image = self.attacking_left
						self.on_cover = False
						self.attack_duration = 10
						self.ready2attack = False
						self.reload_time = 30
						self.on_attack = True
					#Go away if not
					else:
						#Up
						if self.rect.bottom>(self.HEIGHT - 70):
							if self.rect.centery < target.rect.centery:
								if self.look_right:
									self.looking_right.play()
									self.image = self.looking_right.get_current_image()
								elif self.look_left:
									self.looking_left.play()
									self.image = self.looking_left.get_current_image()
								self.rect.centery -= self.speed_x * time
						#Down
						if self.rect.bottom<self.HEIGHT:
							if self.rect.centery > target.rect.centery:
								if self.look_right:
									self.looking_right.play()
									self.image = self.looking_right.get_current_image()
								elif self.look_left:
									self.looking_left.play()
									self.image = self.looking_left.get_current_image()
								self.rect.centery += self.speed_x * time
						#Right
						if self.rect.right<self.WIDTH:
							if target.rect.centerx<self.rect.centerx:
								self.look_left = False
								self.look_right = True
								self.looking_right.play()
								self.image = self.looking_right.get_current_image()
								self.rect.centerx += self.speed_x * time
						#Left
						if self.rect.left>0:
							if target.rect.centerx>self.rect.centerx:
								self.look_left = True
								self.look_right = False
								self.looking_left.play()
								self.image = self.looking_left.get_current_image()
								self.rect.centerx -= self.speed_x * time
		
	def hitBy(self, enemy):
		if self.health > 0 and self.on_damage == False and self.on_stun == False:
			#Force enemy to get damage
			self.on_attack = False
			self.damaged.play()
			
			self.speed_y = -10
			if self.rect.centery <= self.HEIGHT or self.rect.bottom <= self.HEIGHT:
				self.ground = self.HEIGHT - 50
			else:
				self.ground = self.rect.centery
			try:
				if enemy.look_right:
					self.look_right = True
					self.look_left = False
				elif enemy.look_left:
					self.look_right = False
					self.look_left = True
			except:
				if self.look_right:
					self.look_left = True
					self.look_right = False
				elif self.look_left:
					self.look_right = True
					self.look_left = False
				
			if self.on_cover == False: #Non blocked hit
				self.hit.get_sfx().play()
				self.image = self.damaged.get_current_image()
				self.health -= enemy.power - (enemy.power * self.resistance)
				self.on_damage = True
				self.speed_taken = (enemy.power * 0.5) - (enemy.power * self.resistance)
				
			if self.on_cover:             #Blocked hit
				self.speed_y += 7
				self.speed_taken = (enemy.power * 1.3) - (enemy.power * self.resistance)
				self.health -= enemy.power - (enemy.power * (self.resistance + 0.45))
			
			if enemy.power - (enemy.power * self.resistance) >= 8:   #Stun hit
				if type(enemy) is Tlaloc: #Electrified by Tlaloc
					self.image = self.electrified
				elif type(enemy) is Xiuhtecuhtli: #Burned by Xiuhtecuhtli
					self.image = self.burnt
				else:
					self.image = self.stunned
				self.ground = self.rect.bottom
				self.speed_taken = enemy.power * 2.3
				self.stun_duration = enemy.power * 10
				self.speed_taken = (enemy.power * 2) - (enemy.power * self.resistance)
				self.health -= enemy.power - (enemy.power * self.resistance)
				self.on_damage = False
				self.on_stun = True
			
			if self.health <= 0:             #Dead character
				self.image = self.died
				self.ground = self.rect.bottom - 30
				self.speed_taken = enemy.power * 2.3
				self.on_damage = False
			self.on_air = True
				
	def update(self):
		#On attack	
		if self.on_attack:
			if self.attack_duration > 0:
				self.attack_duration -= 1
			else:
				if self.look_left:
					self.image = self.looking_left.get_current_image()
				else:
					self.image = self.looking_right.get_current_image()
				self.on_attack = False
		if self.ready2attack == False:
			if self.reload_time > 0:
				self.reload_time -= 1
			else:
				self.ready2attack = True
		#On air
		if self.on_air:
			if self.rect.centery + self.speed_y < self.ground:
				self.rect.centery += self.speed_y
				self.speed_y += self.gravity
				if self.look_right == True and self.rect.right < self.WIDTH:
					self.rect.centerx += self.speed_taken
				elif self.look_left == True and self.rect.left > 0:
					self.rect.centerx -= self.speed_taken
			else:
				if self.health <= 0 or self.on_stun:
					if self.speed_y > 11:
						self.speed_y *= self.elasticity
				else:
					if self.on_damage:
						self.on_damage = False
					self.rect.centery = self.ground
					self.on_air = False
					if self.look_left:
						self.image = self.looking_left.get_current_image()
					else:
						self.image = self.looking_right.get_current_image()
		#On stun
		if self.on_stun:
			if self.stun_duration > 0:
				self.stun_duration -= 1
			else:
				self.ground = self.rect.top + 30
				self.on_stun = False
				if self.look_left:
					self.image = self.looking_left.get_current_image()
				else:
					self.image = self.looking_right.get_current_image()

class Boss(Enemy):
	def __init__(self, x, y, space):
		self.speed_walk = 0.09
		super(Boss, self).__init__(x, y, space, "crafty")
	
	def update(self):
		self.horse.update(self)
		super(Boss, self).update()
	
	def ai(self, target, time):
		if self.horse.on_ride:
			self.looking_right = self.riding_right
			self.looking_left = self.riding_left
			self.attacking_right = self.right_riding_attack
			self.attacking_left = self.left_riding_attack
			self.attacking_right_far = self.right_riding_shoot
			self.attacking_left_far = self.left_riding_shoot
			self.speed_x = self.horse.speed_x
		else:
			self.attacking_right = self.right_attack
			self.attacking_left = self.left_attack
			self.attacking_right_far = self.right_shoot
			self.attacking_left_far = self.left_shoot
			self.looking_right = self.walking_right
			self.looking_left = self.walking_left
			self.speed_x = self.speed_walk
		super(Boss, self).ai(target, time)
	
	def hitBy(self, enemy):
		if self.horse.on_ride:
			if self.on_damage == False:
				try:
					if enemy.look_right:
						self.look_right = True
						self.look_left = False
					elif enemy.look_left:
						self.look_right = False
						self.look_left = True
				except:
					if self.look_right:
						self.look_left = True
						self.look_right = False
					elif self.look_left:
						self.look_right = True
						self.look_left = False
				#Force enemy to get damage
				self.on_attack = False
				self.damaged.play()
				if enemy.power - (enemy.power * self.resistance) > 8:   #Stun hit
					if type(enemy) is Tlaloc: #Electrified by Tlaloc
						self.image = self.electrified
					elif type(enemy) is Xiuhtecuhtli: #Burned by Xiuhtecuhtli
						self.image = self.burnt
					else:
						self.image = self.stunned
					self.speed_y = -5
					self.stun_duration = enemy.power * 10
					self.speed_taken = (enemy.power * 2) - (enemy.power * self.resistance)
					self.horse.health -= enemy.power - (enemy.power * self.resistance)
					self.on_stun = True			
				else:	
					self.horse.health -= enemy.power - (enemy.power * (self.resistance + 0.45))
					self.image = self.damaged.get_current_image()
					self.on_damage = True
					self.speed_y = -3
				if self.rect.centery <= self.HEIGHT or self.rect.bottom <= self.HEIGHT:
					self.ground = self.HEIGHT - 50
				else:
					self.ground = self.rect.centery
				self.on_air = True
			
		else:
			super(Boss, self).hitBy(enemy)


class Alvarado(Boss):
	def __init__(self, x, y, space):
		#SFX
		self.step = SFX(pygame.mixer.Sound("audio/sfx/spanish/step_2.wav"), 4)
		self.hit = SFX(pygame.mixer.Sound("audio/sfx/spanish/hit_3.wav"))
		self.swoosh = SFX(pygame.mixer.Sound("audio/sfx/spanish/swoosh_1.wav"))
		self.shot = SFX(pygame.mixer.Sound("audio/sfx/spanish/shot_3.wav"))
		
		#Sprites
		self.riding_right = Animate([
		load_image("sprites/spanish/alvarado/right_ride.png", True),
		], 0.5)
		
		self.riding_left = Animate([
		load_image("sprites/spanish/alvarado/left_ride.png", True),
		], 0.5)
		
		self.walking_right = Animate([
		load_image("sprites/spanish/alvarado/right_walk_1.png", True),
		load_image("sprites/spanish/alvarado/right_walk_2.png", True),
		load_image("sprites/spanish/alvarado/right_walk_3.png", True),
		load_image("sprites/spanish/alvarado/right_walk_4.png", True),
		load_image("sprites/spanish/alvarado/right_walk_5.png", True),
		], 1.5)
		
		self.walking_left = Animate([
		load_image("sprites/spanish/alvarado/left_walk_1.png", True),
		load_image("sprites/spanish/alvarado/left_walk_2.png", True),
		load_image("sprites/spanish/alvarado/left_walk_3.png", True),
		load_image("sprites/spanish/alvarado/left_walk_4.png", True),
		load_image("sprites/spanish/alvarado/left_walk_5.png", True),
		], 1.5)
		
		self.breathing_right = Animate([
		load_image("sprites/spanish/alvarado/right_breath_1.png", True),
		load_image("sprites/spanish/alvarado/right_breath_1.png", True),
		load_image("sprites/spanish/alvarado/right_breath_2.png", True),
		], 0.5)
		
		self.breathing_left = Animate([
		load_image("sprites/spanish/alvarado/left_breath_1.png", True),
		load_image("sprites/spanish/alvarado/left_breath_1.png", True),
		load_image("sprites/spanish/alvarado/left_breath_2.png", True),
		], 0.5)
		
		self.damaged = Animate([
		load_image("sprites/spanish/alvarado/damaged_1.png", True),
		load_image("sprites/spanish/alvarado/damaged_2.png", True),
		], 2)
		
		#Using raw names
		self.left_attack = load_image("sprites/spanish/alvarado/left_attack.png", True)
		self.right_attack = load_image("sprites/spanish/alvarado/right_attack.png", True)
		self.right_riding_attack = load_image("sprites/spanish/alvarado/right_riding_attack.png", True)
		self.left_riding_attack = load_image("sprites/spanish/alvarado/left_riding_attack.png", True)
		self.left_shoot = load_image("sprites/spanish/alvarado/left_shoot.png", True)
		self.right_shoot = load_image("sprites/spanish/alvarado/right_shoot.png", True)
		self.right_riding_shoot = load_image("sprites/spanish/alvarado/right_riding_shoot.png", True)
		self.left_riding_shoot = load_image("sprites/spanish/alvarado/left_riding_shoot.png", True)
		
		self.electrified = load_image("sprites/spanish/alvarado/electrified.png", True)
		self.burnt = load_image("sprites/spanish/alvarado/burnt.png", True)
		self.stunned = load_image("sprites/spanish/alvarado/die.png", True)
		self.died = load_image("sprites/spanish/alvarado/die.png", True)
		
		#Horse
		self.horse = Horse1()
		super(Alvarado, self).__init__(x, y, space)
	
	def update(self):
		super(Alvarado, self).update()
	
	def ai(self, target, time):
		super(Alvarado, self).ai(target, time)
	
	def hitBy(self, enemy):
		super(Alvarado, self).hitBy(enemy)
		
class Cortes(Boss):
	def __init__(self, x, y, space):
		#SFX
		self.step = SFX(pygame.mixer.Sound("audio/sfx/spanish/step_2.wav"), 4)
		self.hit = SFX(pygame.mixer.Sound("audio/sfx/spanish/hit_3.wav"))
		self.swoosh = SFX(pygame.mixer.Sound("audio/sfx/spanish/swoosh_1.wav"))
		self.shot = SFX(pygame.mixer.Sound("audio/sfx/spanish/shot_3.wav"))
		
		#Sprites
		self.riding_right = Animate([
		load_image("sprites/spanish/cortes/right_ride.png", True),
		], 0.5)
		
		self.riding_left = Animate([
		load_image("sprites/spanish/cortes/left_ride.png", True),
		], 0.5)
		
		self.walking_right = Animate([
		load_image("sprites/spanish/cortes/right_walk_1.png", True),
		load_image("sprites/spanish/cortes/right_walk_2.png", True),
		load_image("sprites/spanish/cortes/right_walk_3.png", True),
		load_image("sprites/spanish/cortes/right_walk_4.png", True),
		load_image("sprites/spanish/cortes/right_walk_5.png", True),
		], 1.5)
		
		self.walking_left = Animate([
		load_image("sprites/spanish/cortes/left_walk_1.png", True),
		load_image("sprites/spanish/cortes/left_walk_2.png", True),
		load_image("sprites/spanish/cortes/left_walk_3.png", True),
		load_image("sprites/spanish/cortes/left_walk_4.png", True),
		load_image("sprites/spanish/cortes/left_walk_5.png", True),
		], 1.5)
		
		self.breathing_right = Animate([
		load_image("sprites/spanish/cortes/right_breath_1.png", True),
		load_image("sprites/spanish/cortes/right_breath_1.png", True),
		load_image("sprites/spanish/cortes/right_breath_2.png", True),
		], 0.5)
		
		self.breathing_left = Animate([
		load_image("sprites/spanish/cortes/left_breath_1.png", True),
		load_image("sprites/spanish/cortes/left_breath_1.png", True),
		load_image("sprites/spanish/cortes/left_breath_2.png", True),
		], 0.5)
		
		self.damaged = Animate([
		load_image("sprites/spanish/cortes/damaged_1.png", True),
		load_image("sprites/spanish/cortes/damaged_2.png", True),
		], 2)
		
		#Using raw names
		self.left_attack = load_image("sprites/spanish/cortes/left_attack.png", True)
		self.right_attack = load_image("sprites/spanish/cortes/right_attack.png", True)
		self.right_riding_attack = load_image("sprites/spanish/cortes/right_riding_attack.png", True)
		self.left_riding_attack = load_image("sprites/spanish/cortes/left_riding_attack.png", True)
		self.left_shoot = load_image("sprites/spanish/cortes/left_shoot.png", True)
		self.right_shoot = load_image("sprites/spanish/cortes/right_shoot.png", True)
		self.right_riding_shoot = load_image("sprites/spanish/cortes/right_riding_shoot.png", True)
		self.left_riding_shoot = load_image("sprites/spanish/cortes/left_riding_shoot.png", True)
		
		self.electrified = load_image("sprites/spanish/cortes/electrified.png", True)
		self.burnt = load_image("sprites/spanish/cortes/burnt.png", True)
		self.stunned = load_image("sprites/spanish/cortes/die.png", True)
		self.died = load_image("sprites/spanish/cortes/die.png", True)
		
		#Horse
		self.horse = Horse2()
		super(Cortes, self).__init__(x, y, space)
	
	def update(self):
		super(Cortes, self).update()
	
	def ai(self, target, time):
		super(Cortes, self).ai(target, time)
	
	def hitBy(self, enemy):
		super(Cortes, self).hitBy(enemy)


class Spanish1(Enemy):
	def __init__(self, x, y, space):
		#SFX
		self.step = SFX(pygame.mixer.Sound("audio/sfx/spanish/step_2.wav"), 4)
		self.hit = SFX(pygame.mixer.Sound("audio/sfx/spanish/hit_1.wav"))
		self.swoosh = SFX(pygame.mixer.Sound("audio/sfx/spanish/swoosh_1.wav"))
		self.shot = SFX(pygame.mixer.Sound("audio/sfx/spanish/shot_1.wav"))
		
		#Sprites
		self.looking_right = Animate([
		load_image("sprites/spanish/spanish1/right_walk_1.png", True),
		load_image("sprites/spanish/spanish1/right_walk_2.png", True),
		load_image("sprites/spanish/spanish1/right_walk_3.png", True),
		load_image("sprites/spanish/spanish1/right_walk_4.png", True),
		load_image("sprites/spanish/spanish1/right_walk_3.png", True),
		], 1.5)
		
		self.looking_left = Animate([
		load_image("sprites/spanish/spanish1/left_walk_1.png", True),
		load_image("sprites/spanish/spanish1/left_walk_2.png", True),
		load_image("sprites/spanish/spanish1/left_walk_3.png", True),
		load_image("sprites/spanish/spanish1/left_walk_4.png", True),
		load_image("sprites/spanish/spanish1/left_walk_3.png", True),
		], 1.5)
		
		self.breathing_right = Animate([
		load_image("sprites/spanish/spanish1/right_breath_1.png", True),
		load_image("sprites/spanish/spanish1/right_breath_2.png", True),
		], 0.4)
		
		self.breathing_left = Animate([
		load_image("sprites/spanish/spanish1/left_breath_1.png", True),
		load_image("sprites/spanish/spanish1/left_breath_2.png", True),
		], 0.4)
		
		self.damaged = Animate([
		load_image("sprites/spanish/spanish1/damaged_1.png", True),
		load_image("sprites/spanish/spanish1/damaged_2.png", True),
		], 2)
		
		self.attacking_left = load_image("sprites/spanish/spanish1/left_attack.png", True)
		self.attacking_right = load_image("sprites/spanish/spanish1/right_attack.png", True)
		
		self.attacking_left_far = load_image("sprites/spanish/spanish1/left_shoot.png", True)
		self.attacking_right_far = load_image("sprites/spanish/spanish1/right_shoot.png", True)
		
		self.electrified = load_image("sprites/spanish/spanish1/electrified.png", True)
		self.burnt = load_image("sprites/spanish/spanish1/burnt.png", True)
		self.stunned = load_image("sprites/spanish/spanish1/die.png", True)
		self.died = load_image("sprites/spanish/spanish1/die.png", True)
		
		#Enemy attributes
		super(Spanish1, self).__init__(x, y, space, "aggressive")
	
	def update(self):
		super(Spanish1, self).update()
	
	def ai(self, target, time):
		super(Spanish1, self).ai(target, time)
	
	def hitBy(self, enemy):
		super(Spanish1, self).hitBy(enemy)
		

class Spanish2(Enemy):
	def __init__(self, x, y, space):
		#SFX
		self.step = SFX(pygame.mixer.Sound("audio/sfx/spanish/step_3.wav"), 4)
		self.hit = SFX(pygame.mixer.Sound("audio/sfx/spanish/hit_4.wav"))
		self.swoosh = SFX(pygame.mixer.Sound("audio/sfx/spanish/swoosh_2.wav"))
		self.shot = SFX(pygame.mixer.Sound("audio/sfx/spanish/shot_2.wav"))
		
		#Sprites
		self.looking_right = Animate([
		load_image("sprites/spanish/spanish2/right_walk_1.png", True),
		load_image("sprites/spanish/spanish2/right_walk_2.png", True),
		load_image("sprites/spanish/spanish2/right_walk_3.png", True),
		load_image("sprites/spanish/spanish2/right_walk_4.png", True),
		load_image("sprites/spanish/spanish2/right_walk_3.png", True),
		], 1.5)
		
		self.looking_left = Animate([
		load_image("sprites/spanish/spanish2/left_walk_1.png", True),
		load_image("sprites/spanish/spanish2/left_walk_2.png", True),
		load_image("sprites/spanish/spanish2/left_walk_3.png", True),
		load_image("sprites/spanish/spanish2/left_walk_4.png", True),
		load_image("sprites/spanish/spanish2/left_walk_3.png", True),
		], 1.5)
		
		self.breathing_right = Animate([
		load_image("sprites/spanish/spanish2/right_breath_1.png", True),
		load_image("sprites/spanish/spanish2/right_breath_1.png", True),
		load_image("sprites/spanish/spanish2/right_breath_2.png", True),
		], 0.3)
		
		self.breathing_left = Animate([
		load_image("sprites/spanish/spanish2/left_breath_1.png", True),
		load_image("sprites/spanish/spanish2/left_breath_1.png", True),
		load_image("sprites/spanish/spanish2/left_breath_2.png", True),
		], 0.3)
		
		self.damaged = Animate([
		load_image("sprites/spanish/spanish2/damaged_1.png", True),
		load_image("sprites/spanish/spanish2/damaged_2.png", True),
		], 2)
		
		self.attacking_left = load_image("sprites/spanish/spanish2/left_attack.png", True)
		self.attacking_right = load_image("sprites/spanish/spanish2/right_attack.png", True)
		
		self.attacking_left_far = load_image("sprites/spanish/spanish2/left_shoot.png", True)
		self.attacking_right_far = load_image("sprites/spanish/spanish2/right_shoot.png", True)
		
		self.electrified = load_image("sprites/spanish/spanish2/electrified.png", True)
		self.burnt = load_image("sprites/spanish/spanish2/burnt.png", True)
		self.stunned = load_image("sprites/spanish/spanish2/die.png", True)
		self.died = load_image("sprites/spanish/spanish2/die.png", True)
		
		#Enemy attributes
		super(Spanish2, self).__init__(x, y, space, "crafty")
	
	def update(self):
		super(Spanish2, self).update()
	
	def ai(self, target, time):
		super(Spanish2, self).ai(target, time)
	
	def hitBy(self, enemy):
		super(Spanish2, self).hitBy(enemy)


class Spanish3(Enemy):
	def __init__(self, x, y, space):
		#SFX
		self.step = SFX(pygame.mixer.Sound("audio/sfx/spanish/step_2.wav"), 4)
		self.hit = SFX(pygame.mixer.Sound("audio/sfx/spanish/hit_3.wav"))
		self.swoosh = SFX(pygame.mixer.Sound("audio/sfx/spanish/swoosh_1.wav"))
		self.shot = SFX(pygame.mixer.Sound("audio/sfx/spanish/shot_3.wav"))
		
		#Sprites
		self.looking_right = Animate([
		load_image("sprites/spanish/spanish3/right_walk_1.png", True),
		load_image("sprites/spanish/spanish3/right_walk_2.png", True),
		load_image("sprites/spanish/spanish3/right_walk_3.png", True),
		], 1.5)
		
		self.looking_left = Animate([
		load_image("sprites/spanish/spanish3/left_walk_1.png", True),
		load_image("sprites/spanish/spanish3/left_walk_2.png", True),
		load_image("sprites/spanish/spanish3/left_walk_3.png", True),
		], 1.5)
		
		self.breathing_right = Animate([
		load_image("sprites/spanish/spanish3/right_breath_1.png", True),
		load_image("sprites/spanish/spanish3/right_breath_1.png", True),
		load_image("sprites/spanish/spanish3/right_breath_2.png", True),
		], 0.5)
		
		self.breathing_left = Animate([
		load_image("sprites/spanish/spanish3/left_breath_1.png", True),
		load_image("sprites/spanish/spanish3/left_breath_1.png", True),
		load_image("sprites/spanish/spanish3/left_breath_2.png", True),
		], 0.5)
		
		self.damaged = Animate([
		load_image("sprites/spanish/spanish3/damaged_1.png", True),
		load_image("sprites/spanish/spanish3/damaged_2.png", True),
		], 2)
		
		self.attacking_left = load_image("sprites/spanish/spanish3/left_attack.png", True)
		self.attacking_right = load_image("sprites/spanish/spanish3/right_attack.png", True)
		
		self.attacking_left_far = load_image("sprites/spanish/spanish3/left_shoot.png", True)
		self.attacking_right_far = load_image("sprites/spanish/spanish3/right_shoot.png", True)
		
		self.electrified = load_image("sprites/spanish/spanish3/electrified.png", True)
		self.burnt = load_image("sprites/spanish/spanish3/burnt.png", True)
		self.stunned = load_image("sprites/spanish/spanish3/die.png", True)
		self.died = load_image("sprites/spanish/spanish3/die.png", True)
		
		#Enemy attributes
		super(Spanish3, self).__init__(x, y, space, "coward")
	
	def update(self):
		super(Spanish3, self).update()
	
	def ai(self, target, time):
		super(Spanish3, self).ai(target, time)
	
	def hitBy(self, enemy):
		super(Spanish3, self).hitBy(enemy)
