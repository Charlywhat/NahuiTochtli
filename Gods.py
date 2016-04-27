import pygame
from pygame.locals import *
from Animate import Animate
from Animate import SFX
import random
from Camera import load_image

class God(pygame.sprite.Sprite):
	def __init__(self, x, y, space):
		pygame.sprite.Sprite.__init__(self)
		#Sprites
		self.none = load_image("sprites/gods/god/none.png", True)
		
		#Position and space
		self.WIDTH = space[0]
		self.HEIGHT = space[1]
		self.image = self.idle
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		
		#States
		self.invokable = True
		self.on_invoke = False
		self.on_action = False
		self.on_sub_action = False
		
		#Attributes
		self.power = 20
		self.health = 100
		self.reload_time = 0
		self.sub_action_duration = 0
		self.sub_action_target = None
		self.sub_action_target_pos = None
		
	
	def invoked(self, invoker):
		self.on_invoke = True
		self.invoke_duration = invoker.invoke_duration
		self.invokable = False
		
	
	def update(self, invoker, enemies):
		if self.on_invoke == True:
			self.being_invoked.play()
			self.image = self.being_invoked.get_current_image()
			if self.invoke_duration > 0:
				self.invoke_duration -= 1
			else:
				#End of invocation / Start action
				self.being_invoked.stop()
				self.on_invoke = False
				self.on_action = True
				self.image = self.none


class Ehecatl(God):
	def __init__(self, x, y, space):
		#Ehecatl attributes
		self.wind = SFX(pygame.mixer.Sound("audio/sfx/gods/ehecatl/wind.wav"))
		self.idle = load_image("sprites/gods/ehecatl/idle.png", True)
		self.being_invoked = Animate([
		load_image("sprites/gods/ehecatl/invoked_1.png", True),
		load_image("sprites/gods/ehecatl/invoked_2.png", True),
		load_image("sprites/gods/ehecatl/invoked_3.png", True),
		load_image("sprites/gods/ehecatl/invoked_4.png", True),
		load_image("sprites/gods/ehecatl/invoked_5.png", True),], 3)
		self.tornado = Animate([
		load_image("sprites/gods/ehecatl/tornado_1.png", True),
		load_image("sprites/gods/ehecatl/tornado_2.png", True),
		load_image("sprites/gods/ehecatl/tornado_3.png", True),
		load_image("sprites/gods/ehecatl/tornado_4.png", True),
		load_image("sprites/gods/ehecatl/tornado_5.png", True),
		load_image("sprites/gods/ehecatl/tornado_6.png", True),], 2.5)
		#Super class attributes
		super(Ehecatl, self).__init__(x, y, space)

	def update(self, invoker, enemies):
		#Super class actions
		super(Ehecatl, self).update(invoker, enemies)
		
		#Ehecatl actions
		if self.on_action == True:
			if self.health > 0:
				if self.wind.is_playing() == False: self.wind.get_sfx().play()
				self.tornado.play()
				self.image = self.tornado.get_current_image() #Tornado animation
				#Make invoker jump longer
				invoker.gravity = 0.8
				
				#Ehecatl will always attack
				self.on_sub_action = True
				self.rect.centerx = invoker.rect.centerx - 20
				self.rect.bottom = invoker.rect.bottom + 1
				if self.sub_action_duration > 0:
					for enemy in enemies:
						if abs(enemy.rect.centerx - self.rect.centerx) < 250:
							self.sub_action_target = enemy
					self.sub_action_duration -= 1
				else:
					self.sub_action_duration = 10
					self.health -= 1
			else:
				self.wind.get_sfx().fadeout(100)
				self.on_sub_action = False
				self.on_action = False
				self.image = self.none
				invoker.gravity = 1.3	


class Tezcatlipoca(God):
	pass

class Xiuhtecuhtli(God):
	def __init__(self, x, y, space):
		#SFX
		self.asteroid_sound = SFX(pygame.mixer.Sound("audio/sfx/gods/xiuhtecuhtli/fireball_1.wav"))
		self.asteroid_explosion = SFX(pygame.mixer.Sound("audio/sfx/gods/xiuhtecuhtli/explosion_1.wav"))
		
		#Sprites
		self.idle = load_image("sprites/gods/xiuhtecuhtli/idle.png", True)
		self.being_invoked = Animate([
		load_image("sprites/gods/xiuhtecuhtli/invoked_1.png", True),
		load_image("sprites/gods/xiuhtecuhtli/invoked_2.png", True),
		load_image("sprites/gods/xiuhtecuhtli/invoked_3.png", True),
		load_image("sprites/gods/xiuhtecuhtli/invoked_4.png", True),
		load_image("sprites/gods/xiuhtecuhtli/invoked_5.png", True),
		], 2)
		
		self.asteroid_left = Animate([
		load_image("sprites/gods/xiuhtecuhtli/asteroid_left_1.png", True),
		load_image("sprites/gods/xiuhtecuhtli/asteroid_left_2.png", True),
		load_image("sprites/gods/xiuhtecuhtli/asteroid_left_3.png", True),
		load_image("sprites/gods/xiuhtecuhtli/asteroid_left_4.png", True),
		],4)
		
		self.asteroid_right = Animate([
		load_image("sprites/gods/xiuhtecuhtli/asteroid_right_1.png", True),
		load_image("sprites/gods/xiuhtecuhtli/asteroid_right_2.png", True),
		load_image("sprites/gods/xiuhtecuhtli/asteroid_right_3.png", True),
		load_image("sprites/gods/xiuhtecuhtli/asteroid_right_4.png", True),
		],4)
		
		self.explode = Animate([
		load_image("sprites/gods/xiuhtecuhtli/explotion_1.png", True),
		load_image("sprites/gods/xiuhtecuhtli/explotion_2.png", True),
		load_image("sprites/gods/xiuhtecuhtli/explotion_3.png", True),
		load_image("sprites/gods/xiuhtecuhtli/explotion_4.png", True),
		load_image("sprites/gods/xiuhtecuhtli/explotion_5.png", True),
		load_image("sprites/gods/xiuhtecuhtli/explotion_6.png", True),
		],4)
		
		#Super class attributes
		super(Xiuhtecuhtli,self).__init__(x, y, space)
		self.ground = self.HEIGHT - 50
		self.explode_duration = 50
		self.speed_x = 0
		self.speed_y = 8
		
	def update(self, invoker, enemies):
		#Super class actions
		super(Xiuhtecuhtli, self).update(invoker, enemies)
		
		#Xiuhtecuhtli actions
		if self.on_action == True:
			if self.health > 0:
				#Reload
				if self.reload_time > 0:
					self.image = self.none #Hidden while reloading
					self.reload_time -= 1
				#Attack
				else:
					#Continue to attack
					if self.on_sub_action == True:
						self.asteroid_sound.get_sfx().play()
						#Verify direction
						if self.speed_x <= 0:
							self.asteroid_left.play()
							self.image = self.asteroid_left.get_current_image()
						else:
							self.asteroid_right.play()
							self.image = self.asteroid_right.get_current_image()
						#Line equation while falling: m = y/x
						if self.rect.bottom < self.ground:
							self.rect.centerx +=  self.speed_x
							self.rect.bottom += self.speed_y
						#Explode
						else:
							self.asteroid_explosion.get_sfx().play()
							self.asteroid_sound.get_sfx().stop()
							self.asteroid_left.stop()
							self.asteroid_right.stop()
							self.explode.play()
							if self.explode_duration > 0:
								for enemy in enemies:
									if abs(enemy.rect.centerx - self.rect.centerx) < 400:
										self.sub_action_target = enemy
								self.image = self.explode.get_current_image()
								self.explode_duration -= 1
							else:
								self.on_sub_action = False
					#Prepare new attack
					else:
						i = 0
						while i < len(enemies):
							#Select enemy randomly
							rdm = random.randint(0, len(enemies)-1)
							if enemies[rdm].health > 0 and enemies[rdm].on_stun == False:
								#Verify that enemy is visible
								if abs(enemies[rdm].rect.centerx - invoker.rect.centerx) < 500:
									break
							i += 1
						self.sub_action_target = enemies[rdm]
						#Set lock on target
						self.sub_action_target_pos = self.sub_action_target.rect.centerx
						self.rect.centerx = self.WIDTH / 2
						self.rect.bottom = 0
						self.speed_x = float((self.speed_y) * (self.sub_action_target_pos - self.rect.centerx)) / self.ground
						#Restart timers
						self.reload_time = 100
						self.explode_duration = 10
						self.on_sub_action = True
						self.health -= 10
			else:
				self.on_action = False
				self.image = self.none
			

class Quetzalcoatl(God):
	def __init__(self, x, y, space):
		#Quetzalcoatl attributes
		self.idle = load_image("sprites/gods/quetzalcoatl/idle.png", True)
		self.being_invoked = Animate([
		load_image("sprites/gods/quetzalcoatl/invoked_1.png", True),
		load_image("sprites/gods/quetzalcoatl/invoked_2.png", True),
		load_image("sprites/gods/quetzalcoatl/invoked_3.png", True),
		load_image("sprites/gods/quetzalcoatl/invoked_4.png", True),
		load_image("sprites/gods/quetzalcoatl/invoked_5.png", True),], 2)
		
		self.healing = Animate([
		load_image("sprites/gods/quetzalcoatl/heal_1.png", True),
		load_image("sprites/gods/quetzalcoatl/heal_2.png", True),
		load_image("sprites/gods/quetzalcoatl/heal_3.png", True),
		load_image("sprites/gods/quetzalcoatl/heal_4.png", True),
		load_image("sprites/gods/quetzalcoatl/heal_5.png", True),
		],3)
		
		#Super class attributes
		super(Quetzalcoatl, self).__init__(x, y, space)

	def update(self, invoker, enemies):
		#Super class actions
		super(Quetzalcoatl, self).update(invoker, enemies)
		
		#Quetzalcoatl actions
		if self.on_action == True:
			if self.health > 0:
				self.healing.play()
				self.image = self.healing.get_current_image()
				self.rect.centerx = invoker.rect.centerx - 15
				self.rect.centery = invoker.rect.centery + 1
				if self.sub_action_duration > 0:
					self.sub_action_duration -= 1
				else:
					self.sub_action_duration = 1
					self.health -= 5
			else:
				self.on_action = False
				invoker.health = 100
				self.image = self.none	

class Huitzilopochtli(God):
	def __init__(self, x, y, space):
		#Huitzilopochtli attributes
		self.idle = load_image("sprites/gods/huitzilopochtli/idle.png", True)
		self.being_invoked = Animate([
		load_image("sprites/gods/huitzilopochtli/invoked_1.png", True),
		load_image("sprites/gods/huitzilopochtli/invoked_2.png", True),
		load_image("sprites/gods/huitzilopochtli/invoked_3.png", True),
		load_image("sprites/gods/huitzilopochtli/invoked_4.png", True),
		load_image("sprites/gods/huitzilopochtli/invoked_5.png", True),], 2)
		
		self.breathing_right = Animate([
		load_image("sprites/gods/huitzilopochtli/right_breath_1.png", True),
		load_image("sprites/gods/huitzilopochtli/right_breath_1.png", True),
		load_image("sprites/gods/huitzilopochtli/right_breath_2.png", True)
		], 0.4)
		
		self.breathing_left = Animate([
		load_image("sprites/gods/huitzilopochtli/left_breath_1.png", True),
		load_image("sprites/gods/huitzilopochtli/left_breath_1.png", True),
		load_image("sprites/gods/huitzilopochtli/left_breath_2.png", True),
		], 0.4)
		
		self.looking_right = Animate([
		load_image("sprites/gods/huitzilopochtli/right_walk_1.png", True),
		load_image("sprites/gods/huitzilopochtli/right_walk_2.png", True),
		load_image("sprites/gods/huitzilopochtli/right_walk_3.png", True),
		load_image("sprites/gods/huitzilopochtli/right_walk_2.png", True),
		], 2)
		
		self.looking_left = Animate([
		load_image("sprites/gods/huitzilopochtli/left_walk_1.png", True),
		load_image("sprites/gods/huitzilopochtli/left_walk_2.png", True),
		load_image("sprites/gods/huitzilopochtli/left_walk_3.png", True),
		load_image("sprites/gods/huitzilopochtli/left_walk_2.png", True),
		], 2)
		
		self.attacking_right_1 = load_image("sprites/gods/huitzilopochtli/right_attack_1.png", True)
		self.attacking_right_2 = load_image("sprites/gods/huitzilopochtli/right_attack_2.png", True)
		self.attacking_right_3 = load_image("sprites/gods/huitzilopochtli/right_attack_3.png", True)
		self.attacking_right_4 = load_image("sprites/gods/huitzilopochtli/right_attack_4.png", True)
		self.attacking_right_air = load_image("sprites/gods/huitzilopochtli/right_attack_air.png", True)
		
		self.attacking_left_1 = load_image("sprites/gods/huitzilopochtli/left_attack_1.png", True)
		self.attacking_left_2 = load_image("sprites/gods/huitzilopochtli/left_attack_2.png", True)
		self.attacking_left_3 = load_image("sprites/gods/huitzilopochtli/left_attack_3.png", True)
		self.attacking_left_4 = load_image("sprites/gods/huitzilopochtli/left_attack_4.png", True)
		self.attacking_left_air = load_image("sprites/gods/huitzilopochtli/left_attack_air.png", True)
		
		self.jumping_right = load_image("sprites/gods/huitzilopochtli/right_jump.png", True)
		self.jumping_left = load_image("sprites/gods/huitzilopochtli/left_jump.png", True)
		
		self.invoking = load_image("sprites/gods/huitzilopochtli/invoke.png", True)
		self.covered = load_image("sprites/gods/huitzilopochtli/cover.png", True)
		self.died = load_image("sprites/gods/huitzilopochtli/die.png", True)
		self.stunned = load_image("sprites/gods/huitzilopochtli/die.png", True)
		self.damaged = load_image("sprites/gods/huitzilopochtli/damaged.png", True)
		
		#Super class attributes
		super(Huitzilopochtli, self).__init__(x, y, space)

	def update(self, invoker, enemies):
		#Super class actions
		super(Huitzilopochtli, self).update(invoker, enemies)
		
		#Huitzilopotchtli actions
		if self.on_action == True:
			invoker.power = 10
			invoker.resistance = 0.85
			if self.health > 0:
				self.rect.centerx = invoker.rect.centerx
				self.rect.centery = invoker.rect.centery
				
				#Huitzilopochtli copies invoker moves
				#Invoker actions
				#Force death when health reaches 0
				if invoker.health <= 0:
					invoker.image = self.died
				else:
					#Breath when static
					if invoker.on_move == False:
						if invoker.on_attack == False:
							if invoker.on_air == False:
								if invoker.on_damage == False:
									if invoker.on_cover == False:
										if invoker.look_right == True:
											self.breathing_right.play()
											invoker.image = self.breathing_right.get_current_image()
										else:
											self.breathing_left.play()
											invoker.image = self.breathing_left.get_current_image()
					#Moving right or left
					if invoker.on_move == True:
						if invoker.look_right == True:
							self.looking_right.play()
							invoker.image = self.looking_right.get_current_image()
						else:
							self.looking_left.play()
							invoker.image = self.looking_left.get_current_image()
					
					#Jumping
					if invoker.on_air == True and invoker.health > 0:
						if invoker.on_damage == False and invoker.on_stun == False:
							if invoker.look_right == True:
								invoker.image = self.jumping_right
							elif invoker.look_left == True:
								invoker.image = self.jumping_left
					
					#Attacking
					if invoker.on_attack == True:
						#Right
						if invoker.look_right == True:
							if invoker.combo_attack == 1:
								invoker.image = self.attacking_right_1
							if invoker.combo_attack == 2:
								invoker.image = self.attacking_right_2
							if invoker.combo_attack == 3:
								invoker.image = self.attacking_right_3
							if invoker.combo_attack == 4:
								invoker.power = 12
								invoker.image = self.attacking_right_4
							if invoker.on_air == True:
								invoker.image = self.attacking_right_air
						#Left
						if invoker.look_left == True:
							if invoker.combo_attack == 1:
								invoker.image = self.attacking_left_1
							if invoker.combo_attack == 2:
								invoker.image = self.attacking_left_2
							if invoker.combo_attack == 3:
								invoker.image = self.attacking_left_3
							if invoker.combo_attack == 4:
								invoker.power = 12
								invoker.image = self.attacking_left_4
							if invoker.on_air == True:
								invoker.image = self.attacking_left_air
					
					#Damaged or Stunned
					if invoker.on_damage == True:
						invoker.image = self.damaged
					if invoker.on_stun == True:
						invoker.image = self.stunned
					
					#Covered or Invoking
					if invoker.on_invoke == True:
						invoker.image = self.invoking
					if invoker.on_cover == True:
						invoker.image = self.covered
							
						
				if self.sub_action_duration > 0:
					self.sub_action_duration -= 1
				else:
					self.sub_action_duration = 10
					self.health -= 1
			else:
				self.on_action = False
				invoker.power = 6
				invoker.resistance = 0.55
				self.image = self.none	
	
class Tlaloc(God):
	def __init__(self, x, y, space):
		#Tlaloc attributes
		self.thunder = [
		SFX(pygame.mixer.Sound("audio/sfx/gods/tlaloc/lightning_1.wav"), 19),
		SFX(pygame.mixer.Sound("audio/sfx/gods/tlaloc/lightning_2.wav"), 19),
		SFX(pygame.mixer.Sound("audio/sfx/gods/tlaloc/lightning_3.wav"), 19),
		]
		random.seed()
		self.idle = load_image("sprites/gods/tlaloc/idle.png", True)
		self.cloud_attack = Animate([
		load_image("sprites/gods/tlaloc/cloud_attack_1.png", True),
		load_image("sprites/gods/tlaloc/cloud_attack_2.png", True),
		load_image("sprites/gods/tlaloc/cloud_attack_3.png", True),
		load_image("sprites/gods/tlaloc/cloud_attack_4.png", True),], 3)
		self.being_invoked = Animate([
		load_image("sprites/gods/tlaloc/invoked_1.png", True),
		load_image("sprites/gods/tlaloc/invoked_2.png", True),
		load_image("sprites/gods/tlaloc/invoked_3.png", True),
		load_image("sprites/gods/tlaloc/invoked_4.png", True),
		load_image("sprites/gods/tlaloc/invoked_5.png", True),], 2)
		self.cloud = Animate([
		load_image("sprites/gods/tlaloc/cloud_1.png", True),
		load_image("sprites/gods/tlaloc/cloud_2.png", True),
		load_image("sprites/gods/tlaloc/cloud_3.png", True),
		load_image("sprites/gods/tlaloc/cloud_4.png", True),], 1)
		
		#Super class attributes
		super(Tlaloc, self).__init__(x, y, space)

	def update(self, invoker, enemies):
		#Super class actions
		super(Tlaloc, self).update(invoker, enemies)
		
		#Tlaloc actions
		if self.on_action == True:
			if self.health > 0:
				self.rect.top = 0
				#Reload
				if self.reload_time > 0:
					self.cloud.play()
					self.image = self.cloud.get_current_image()
					self.rect = self.image.get_rect()
					self.rect.centerx = invoker.rect.centerx
					self.reload_time -= 1
				#Attack
				else:
					#Continue to attack
					if self.sub_action_duration > 0:
						#SFX thunder
						rdm = random.randint(0,2)
						if self.thunder[rdm].is_playable(): self.thunder[rdm].get_sfx().play()
						for t in self.thunder: t.update()
						self.cloud_attack.play()
						self.image = self.cloud_attack.get_current_image()
						self.rect = self.image.get_rect()
						self.rect.centerx = self.sub_action_target_pos
						self.on_sub_action = True
						self.sub_action_duration -= 1
					#Prepare new attack
					else:
						i = 0
						while i < len(enemies):
							#Select enemy randomly
							rdm = random.randint(0, len(enemies)-1)
							if enemies[rdm].health > 0 and enemies[rdm].on_stun == False:
								#Verify that enemy is visible
								if abs(enemies[rdm].rect.centerx - invoker.rect.centerx) < 500:
									break
							i += 1
						self.sub_action_target = enemies[rdm]
						self.cloud_attack.stop()
						#Set lock on target
						self.sub_action_target_pos = self.sub_action_target.rect.centerx
						#Restart timers
						self.sub_action_duration = 10
						self.reload_time = 100
						self.on_sub_action = False
					self.health -= 1
			else:
				self.on_action = False
				self.on_sub_action = False
				self.image = self.none

class Mictlantecuhtli(God):
	def __init__(self, x, y, space):
		#Mictlantecuhtli attributes
		self.idle = load_image("sprites/gods/mictlantecuhtli/idle.png", True)
		self.being_invoked = Animate([
		load_image("sprites/gods/mictlantecuhtli/invoked_1.png", True),
		load_image("sprites/gods/mictlantecuhtli/invoked_2.png", True),
		load_image("sprites/gods/mictlantecuhtli/invoked_3.png", True),
		load_image("sprites/gods/mictlantecuhtli/invoked_4.png", True),
		load_image("sprites/gods/mictlantecuhtli/invoked_5.png", True),], 3)
		
		self.killing = Animate([
		load_image("sprites/gods/mictlantecuhtli/kill_1.png", True),
		load_image("sprites/gods/mictlantecuhtli/kill_2.png", True),
		load_image("sprites/gods/mictlantecuhtli/kill_3.png", True),
		load_image("sprites/gods/mictlantecuhtli/kill_4.png", True),
		load_image("sprites/gods/mictlantecuhtli/kill_5.png", True),
		],3)
		
		#Super class attributes
		super(Mictlantecuhtli, self).__init__(x, y, space)

	def update(self, invoker, enemies):
		#Super class actions
		super(Mictlantecuhtli, self).update(invoker, enemies)
		
		#Mictlantcuhtli actions
		if self.on_action == True:
			if self.health > 0:
				self.killing.play()
				self.image = self.killing.get_current_image()
				self.rect.centerx = invoker.rect.centerx - 15
				self.rect.centery = invoker.rect.centery + 1
				if self.sub_action_duration > 0:
					self.sub_action_duration -= 1
				else:
					self.sub_action_duration = 1
					self.health -= 5
			else:
				self.on_action = False
				invoker.health = 0
				self.image = self.none	

