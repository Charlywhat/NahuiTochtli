import random
import os
import pygame
from pygame.locals import *

from Animate import SFX
from Camera import Camera
from Camera import load_image
from Camera import back2front
from NahuiTochtli import NahuiTochtli
from Enemy import Spanish1
from Enemy import Spanish2
from Enemy import Spanish3
from Enemy import Alvarado
from Enemy import Cortes
from Codex import Codex

from Gods import Ehecatl
from Gods import Tlaloc
from Gods import Huitzilopochtli
from Gods import Quetzalcoatl
from Gods import Tezcatlipoca
from Gods import Mictlantecuhtli
from Gods import Xiuhtecuhtli

WIDTH = 900
HEIGHT = 480
LEVEL_WIDTH = 1900
LEVEL_HEIGHT = HEIGHT

def get_levels():
	print "Loading..."
	#Home directory
	home_directory = os.path.expanduser('~')
	if not os.path.exists(home_directory+'/.nahuitochtli'):
		os.makedirs(home_directory+'/.nahuitochtli')
	home_directory += '/.nahuitochtli/'
	try:
		f = open(home_directory+"lvl")
		hl = f.readline()
		f.close()
	except Exception, e:
		print "Oops! "+str(e)
		hl = 1
		f = open(home_directory+"lvl", 'w')
		f.write(str(hl)+'\n')
		f.close()
	if int(hl) >= 12 or not hl: hl = 1
	print "Current level: "+str(hl)
	return int(hl)

def save_level(l):
	#Home directory
	home_directory = os.path.expanduser('~')
	if not os.path.exists(home_directory+'/.nahuitochtli'):
		os.makedirs(home_directory+'/.nahuitochtli')
	home_directory += '/.nahuitochtli/'
	try: os.remove(home_directory+"lvl")
	except: pass
	f = open(home_directory+"lvl", 'w')
	print "Saving..."
	f.write(str(l)+'\n')
	f.close()
	print "OK"

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+(WIDTH/2), -t+(HEIGHT/2), w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)

class Level():
	def __init__(self, ln=1):
		random.seed()
		self.level_number = ln
		self.delay = 100  #A bit delay after level is completed
		music_veracruz = SFX(pygame.mixer.Sound("audio/music/veracruz.wav"))
		music_puebla = SFX(pygame.mixer.Sound("audio/music/puebla.wav"))
		music_tenochtitlan = SFX(pygame.mixer.Sound("audio/music/tenochtitlan.wav"))
		music_alvarado = SFX(pygame.mixer.Sound("audio/music/alvarado.wav"))
		music_cortes = SFX(pygame.mixer.Sound("audio/music/cortes.wav"))
		self.music = music_veracruz
		
		#Level 1--------------------------------------------------------
		if self.level_number == 1:
			#Level music
			self.music = music_veracruz
			
			#No gods
			self.Teo = []
			
			#Nahui
			self.Nahui = NahuiTochtli(1, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT))
			
			#Enemies
			self.NoE = 1
			self.Enem = []
			
			self.Enem.append(Spanish1(LEVEL_WIDTH*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
				
				
		#Level 2--------------------------------------------------------
		elif self.level_number == 2:
			#Level music
			self.music = music_veracruz
			
			#Gods
			self.Teo = [
				Quetzalcoatl((LEVEL_WIDTH / 2), LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				]
			
			#Nahui
			self.Nahui = NahuiTochtli(1, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT))
			
			#Enemies
			self.NoE = 2
			self.Enem = []
			
			self.Enem.append(Spanish1(LEVEL_WIDTH/1, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH/2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
		
		#Level 3--------------------------------------------------------
		elif self.level_number == 3:
			#Level music
			self.music = music_veracruz
			
			#Gods
			self.Teo = [
				Huitzilopochtli((LEVEL_WIDTH - 20), LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				]
			
			#Nahui
			self.Nahui = NahuiTochtli(LEVEL_WIDTH/2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT))
			
			#Enemies
			self.NoE = 3
			self.Enem = []
			
			self.Enem.append(Spanish1(1, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH-1, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			
		#Level 4--------------------------------------------------------
		elif self.level_number == 4:
			#Level music
			self.music = music_veracruz
			
			#Gods
			self.Teo = [
				Ehecatl(20, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				]
			
			#Nahui
			self.Nahui = NahuiTochtli(LEVEL_WIDTH/2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT))
			
			#Enemies
			self.NoE = 3
			self.Enem = []
			
			self.Enem.append(Spanish1(LEVEL_WIDTH, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/3*2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish3(LEVEL_WIDTH/3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			
		#Level 5--------------------------------------------------------
		elif self.level_number == 5:
			#Puebla music
			self.music = music_puebla
			
			#Gods
			self.Teo = [
				Tlaloc(LEVEL_WIDTH/2, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				]
			
			#Nahui
			self.Nahui = NahuiTochtli(LEVEL_WIDTH - 1, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT))
			
			#Enemies
			self.NoE = 4
			self.Enem = []
			
			self.Enem.append(Spanish1(LEVEL_WIDTH, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH/4*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/4*2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/4, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			
		#Level 6--------------------------------------------------------
		elif self.level_number == 6:
			#Puebla music
			self.music = music_puebla
			
			#Gods
			self.Teo = [
				Huitzilopochtli(LEVEL_WIDTH/2, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				Mictlantecuhtli(LEVEL_WIDTH/3, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				]
			
			#Nahui
			self.Nahui = NahuiTochtli(LEVEL_WIDTH - 1, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT))
			
			#Enemies
			self.NoE = 5
			self.Enem = []
			
			self.Enem.append(Spanish1(LEVEL_WIDTH, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH/5*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH/5*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/5*2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish3(LEVEL_WIDTH/5, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			
		#Level 7--------------------------------------------------------
		elif self.level_number == 7:
			#Puebla music
			self.music = music_puebla
			
			#Gods
			self.Teo = [
				Huitzilopochtli(LEVEL_WIDTH/3*2, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				]
			
			#Nahui
			self.Nahui = NahuiTochtli(LEVEL_WIDTH/2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT))
			
			#Enemies
			self.NoE = 5
			self.Enem = []
			
			self.Enem.append(Spanish3(LEVEL_WIDTH, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH/5*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/5*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/5*2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish3(LEVEL_WIDTH/5, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			
		#Level 8--------------------------------------------------------
		elif self.level_number == 8:
			#Puebla music
			self.music = music_tenochtitlan
			
			#Gods
			self.Teo = [
				Tlaloc(LEVEL_WIDTH/3*2, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				]
			
			#Nahui
			self.Nahui = NahuiTochtli(LEVEL_WIDTH/2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT))
			
			#Enemies
			self.NoE = 6
			self.Enem = []
			
			self.Enem.append(Spanish3(LEVEL_WIDTH, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH/5*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/5*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/5*2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish3(LEVEL_WIDTH/5, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH/5, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			
		#Level 9--------------------------------------------------------
		elif self.level_number == 9:
			#Tenochtiltan music
			self.music = music_tenochtitlan
			
			#Gods
			self.Teo = [
				Mictlantecuhtli(LEVEL_WIDTH/3, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				Ehecatl(LEVEL_WIDTH/3*2, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				]
			
			#Nahui
			self.Nahui = NahuiTochtli(LEVEL_WIDTH, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT))
			
			#Enemies
			self.NoE = 5
			self.Enem = []
			
			self.Enem.append(Spanish1(LEVEL_WIDTH, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH/5*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/5*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/5*2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH/5, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			
		#Level 10--------------------------------------------------------
		elif self.level_number == 10:
			#Tenochtiltan music
			self.music = music_alvarado
			
			#Gods
			self.Teo = [
				Xiuhtecuhtli(LEVEL_WIDTH/3, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				Quetzalcoatl(LEVEL_WIDTH/3*2, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				]
			
			#Nahui
			self.Nahui = NahuiTochtli(1, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT))
			
			#Enemies
			self.NoE = 5
			self.Enem = []
			
			self.Enem.append(Alvarado(LEVEL_WIDTH, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH/5*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/5*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish3(LEVEL_WIDTH/5*2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH/5, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			
		#Level 11--------------------------------------------------------
		elif self.level_number == 11:
			#Tenochtiltan music
			self.music = music_cortes
			
			#Gods
			self.Teo = [
				Xiuhtecuhtli(LEVEL_WIDTH/4, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				Tlaloc(LEVEL_WIDTH/4*2, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				Mictlantecuhtli(LEVEL_WIDTH/4*3, LEVEL_HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)),
				]
			
			#Nahui
			self.Nahui = NahuiTochtli(1, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT))
			
			#Enemies
			self.NoE = 6
			self.Enem = []
			
			self.Enem.append(Cortes(LEVEL_WIDTH, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish3(LEVEL_WIDTH/5*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish3(LEVEL_WIDTH/5*3, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish1(LEVEL_WIDTH/5*2, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish3(LEVEL_WIDTH/5, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
			self.Enem.append(Spanish2(LEVEL_WIDTH/5, HEIGHT, (LEVEL_WIDTH, LEVEL_HEIGHT)))
		
			
		
		for i in range(self.NoE):
			self.Enem[i].speed_x += float(random.randint(0,47) / 100)
		
		#Codex
		self.Cdx = Codex()
		
		#Prepare scene and camera
		self.level_background = Level_Sprite("bg/levels/"+str(self.level_number)+"/bg.png", (0, LEVEL_HEIGHT))
		self.level_foreground = Level_Sprite("bg/levels/"+str(self.level_number)+"/fg.png", (0, LEVEL_HEIGHT))
		self.hud = HUD((LEVEL_WIDTH, LEVEL_HEIGHT))
		self.camera = Camera(complex_camera, LEVEL_WIDTH, LEVEL_HEIGHT)
		
	def codex_update(self):
		self.Cdx.update()
	
	def spanish_move(self, time):
		for i in range(self.NoE):
			self.Enem[i].ai(self.Nahui, time)
			self.Enem[i].update()
	
	def nahui_move(self, time, key, events):
		self.Nahui.move(time,key)
		self.Nahui.update(None)
		for event in events:
			if event.type == KEYUP:
				self.Nahui.update(event.key)
	
	def gods_update(self):
		for god in self.Teo:
			god.update(self.Nahui, self.Enem)
	
	def control_attacks(self):
		for i in range(self.NoE):
			if abs(self.Enem[i].rect.centerx - self.Nahui.rect.centerx) <= 90:
				if self.Nahui.on_attack == True:
					self.Enem[i].hitBy(self.Nahui)
				if self.Enem[i].on_attack == True:
					#Attack when invocation
					if self.Nahui.on_invoke == False:
						self.Nahui.hitBy(self.Enem[i])
					elif self.Nahui.on_invoke == True:
						self.Enem[i].hitBy(self.Nahui)
						
			if abs(self.Enem[i].rect.centery - self.Nahui.rect.centery) < 50:
				if self.Nahui.on_invoke == False:
					if self.Enem[i].on_attack == True:
						self.Nahui.hitBy(self.Enem[i])
			
			for god in self.Teo:
				if god.on_sub_action == True:
					if god.sub_action_target == self.Enem[i]:
						if type(god) is Tlaloc:
							self.Enem[i].hitBy(god)
						if type(god) is Ehecatl:
							self.Enem[i].hitBy(god)
						if type(god) is Xiuhtecuhtli:
							if god.rect.bottom >= god.ground:
								self.Enem[i].hitBy(god)
								
	def control_invocations(self):
		for god in self.Teo:
			if pygame.sprite.collide_rect(self.Nahui, god):
				if self.Nahui.on_cover == True:
					if god.invokable == True:
						self.Nahui.invoke(god)
						god.invoked(self.Nahui)
	
	def focus_camera(self, screen):
		self.camera.update(screen, self.Nahui)
	
	def blit_all(self, screen):
		screen.blit(self.level_background.image, self.camera.apply(self.level_background, False))
		screen.blit(self.level_foreground.image, self.camera.apply(self.level_foreground))
		level_elements = back2front(self.Teo, self.Enem, self.Nahui)
		for i in level_elements:
			screen.blit(i.image, self.camera.apply(i))
	
	def hud_update(self, screen):
		self.hud.update(screen, self.Nahui, self.Teo, self.Cdx)
	
	def play_music(self):
		if not self.music.is_playing():
			self.music.get_sfx().play(-1)
	
	def stop_music(self):
		self.music.get_sfx().fadeout(100)
		
	def update(self, time, key, events, screen):
		self.play_music()
		self.codex_update()
		self.spanish_move(time)
		self.nahui_move(time, key, events)
		self.gods_update()
		self.control_attacks()
		self.control_invocations()
		self.focus_camera(screen)
		self.blit_all(screen)
		self.hud_update(screen)
	
	def completed(self):
		enem_health = []
		for enemy in self.Enem:
			enem_health.append(enemy.health)
			
		if self.Nahui.health <= 0 or all(h <= 0 for h in enem_health):
			if self.delay >= 1:
				self.delay -= 0.5
				return False
			else:
				self.stop_music()
				return True
		else:
			return False
	
	def victory(self):
		if self.Nahui.health > 0: return True
		else: return False
		
class Level_Sprite(pygame.sprite.Sprite):
	def __init__(self, image, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image(image, True)
		self.rect = self.image.get_rect()
		self.rect.left = pos[0]
		self.rect.bottom = pos[1]
		

class HUD(pygame.sprite.Sprite):
	def __init__(self, space):
		pygame.sprite.Sprite.__init__(self)
		self.WIDTH = space[0]
		self.image = load_image("bg/hud/life.png", True)
		self.rect = self.image.get_rect()
		
	def update(self, surface, target, gods, codex):
		#Life update
		pos = [75, 66]
		if target.health >= 50:
			pygame.draw.line(surface, (5.1*abs(target.health - 100),255,0), (pos[0],pos[1]), (pos[0], pos[1]-(0.45*target.health)), 10)
		elif target.health < 50:
			pygame.draw.line(surface, (255,5.1*abs(target.health),0), (pos[0],pos[1]), (pos[0], pos[1]-(0.45*target.health)), 10)
		#Life always at top left corner
		self.rect.top = 5
		self.rect.left = 5
		surface.blit(self.image, self.rect)
		#Current Gods
		pos = [750, -20]
		for g in gods:
			if g.on_action == True:
				g.being_invoked.play()
				surface.blit(g.being_invoked.get_current_image(), pos)
			pos[0] += 15
		#Codex status
		codex.rect.left = 800-abs(codex.health*6.00)
		surface.blit(codex.image, codex.rect, (600-abs(codex.health*6.00),0,600,84))
		codex.flame.rect.right = codex.rect.left
		codex.flame.rect.top = 10
		codex.flame.play()
		surface.blit(codex.flame.get_current_image(), codex.flame.rect)		
