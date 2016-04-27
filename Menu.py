import os
import pygame
from pygame.locals import *

from Camera import load_image
from Animate import SFX

class Label(pygame.sprite.Sprite):
	def __init__(self, cap = "label", pos = (0,0), siz = 13, color = (245,255,245), enabled = True):
		if cap == "\n": cap = ""
		self.caption = cap
		self.enabled = enabled
		self.color = color
		self.no_color = (127,127,127)
		pygame.sprite.Sprite.__init__(self)
		font = pygame.font.Font("bg/menu/dejavu_sans_bold.ttf",siz)
		if self.enabled:
			self.text = pygame.font.Font.render(font, self.caption, 1, self.color)
		else:
			self.text = pygame.font.Font.render(font, self.caption, 1, self.no_color)
		self.rect = self.text.get_rect()
		self.rect.centerx = pos[0]
		self.rect.centery = pos[1]
		
	def click(self, (x,y)):
		if self.enabled:
			if x < (self.rect.centerx + 50) and x > (self.rect.centerx - 50):
				if y < (self.rect.centery + 10) and y > (self.rect.centery - 10):
					return True
	
	def hover(self, (x,y)):
		if x < (self.rect.centerx + 50) and x > (self.rect.centerx - 50):
			if y < (self.rect.centery + 10) and y > (self.rect.centery - 10):
				return True

class Main_Menu():
	def __init__(self, screen):
		#Codices
		#Home directory
		self.home_directory = os.path.expanduser('~')
		if not os.path.exists(self.home_directory+'/.nahuitochtli'):
			os.makedirs(self.home_directory+'/.nahuitochtli')
		self.home_directory += '/.nahuitochtli/'
		try:
			f = open(self.home_directory+"cdx")
			self.all_codices = f.readlines()
			f.close()
		except Exception, e:
			print "Oops! "+str(e)
			self.all_codices = ['0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n', '0\n']
			f = open(self.home_directory+"cdx", 'w')
			for l in self.all_codices: f.write(l)
			f.close()
		self.level_names = {
		1: "Burn the ships!",
		2: "Defend Tajin",
		3: "Cempoala Ambush",
		4: "Escape to Cholula",
		5: "Tlachihualtepetl",
		6: "Liberate Itzocan",
		7: "So long Nexapa",
		8: "Path through Popocatepetl",
		9: "Tenochtitlan",
		10: "Buenas noches Alvarado",
		11: "Senior Cortes",
		}
		#Images
		self.screen = screen
		self.lose = load_image("bg/menu/lose.png", True)
		self.win = load_image("bg/menu/win.png", True)
		self.pause = load_image("bg/menu/pause.png", True)
		self.about = load_image("bg/menu/about.png", True)
		self.mainscreen = load_image("bg/menu/main_menu.png", True)
		self.codices = load_image("bg/menu/codices.png", True)
		self.howtoplay = load_image("bg/menu/howtoplay.png", True)
		self.codex_1 = load_image("bg/codices/codex_1.png", True)
		self.codex_2 = load_image("bg/codices/codex_2.png", True)
		self.codex_3 = load_image("bg/codices/codex_3.png", True)
		self.codex_4 = load_image("bg/codices/codex_4.png", True)
		self.codex_5 = load_image("bg/codices/codex_5.png", True)
		self.codex_6 = load_image("bg/codices/codex_6.png", True)
		self.codex_7 = load_image("bg/codices/codex_7.png", True)
		self.codex_8 = load_image("bg/codices/codex_8.png", True)
		self.codex_9 = load_image("bg/codices/codex_9.png", True)
		self.codex_10 = load_image("bg/codices/codex_10.png", True)
		self.codex_11 = load_image("bg/codices/codex_11.png", True)
		
		self.codex_mask = load_image("bg/codices/mask.png", True)
		self.codex_bg = load_image("bg/codices/bg.png", True)
		
		#Music
		self.lose_music = SFX(pygame.mixer.Sound("audio/music/lose.wav"))
		self.win_music = SFX(pygame.mixer.Sound("audio/music/win.wav"))
		
	def save_codices(self, level_number, codex_health):
		self.all_codices[level_number-1] = str(codex_health)+'\n'
		try: os.remove(self.home_directory+"cdx")
		except: pass
		f = open(self.home_directory+"cdx", 'w')
		for l in self.all_codices: f.write(l)
		f.close()
	
	def blit_menu(self, status, pos, level, events, level_number):
		self.image = getattr(self, status)
		self.rect = self.image.get_rect()
		if status == "mainscreen":
			#Labels
			labs = []
			x = 230
			y = 180
			sz = 17
			m_offset = sz + 15
			offset = 0
			if level_number > 1 and level_number < 12:
				lab_continue = Label("Continue", (pos[0]+x, pos[1]+y+offset), sz, (255,255,255))
			else:
				lab_continue = Label("Continue", (pos[0]+x, pos[1]+y+offset), sz, (255,255,255), enabled = False)
			offset += m_offset
			lab_newgame = Label("New Game", (pos[0]+x, pos[1]+y+offset), sz, (255,255,255))
			offset += m_offset
			lab_codices = Label("Codices", (pos[0]+x, pos[1]+y+offset), sz, (255,255,255))
			offset += m_offset
			lab_howtoplay = Label("How to play", (pos[0]+x, pos[1]+y+offset), sz, (255,255,255))
			offset += m_offset
			lab_about = Label("About", (pos[0]+x, pos[1]+y+offset), sz, (255,255,255))
			offset += m_offset
			lab_quit = Label("Quit", (pos[0]+x, pos[1]+180+offset), sz, (255,255,255))
			labs.append(lab_continue)
			labs.append(lab_newgame)
			labs.append(lab_codices)
			labs.append(lab_howtoplay)
			labs.append(lab_about)
			labs.append(lab_quit)
			#Blit
			self.screen.blit(self.image, pos)
			for lab in labs:
				self.screen.blit(lab.text, lab.rect)
			
			#Return option
			for event in events:
				if event.type == MOUSEBUTTONDOWN:
					if lab_continue.click(event.pos): return 1
					if lab_newgame.click(event.pos): return 0
					if lab_codices.click(event.pos): return 2
					if lab_howtoplay.click(event.pos): return 3
					if lab_about.click(event.pos): return 4
					if lab_quit.click(event.pos): return -1
			
			
		if status == "lose":
			labs = []
			x = 150
			y = 370
			offset = 600
			lab_tryagain = Label("Try Again", (pos[0]+x,pos[1]+y), 28, (255,255,255))
			lab_mainmenu = Label("Main Menu", (pos[0]+x+offset,pos[1]+y), 28, (255,255,255))
			labs.append(lab_tryagain)
			labs.append(lab_mainmenu)
			#Blit
			if self.lose_music.is_playing() == False:
				self.lose_music.get_sfx().play()
			level.blit_all(self.screen)
			self.screen.blit(self.image, pos)
			for lab in labs:
				self.screen.blit(lab.text, lab.rect)
			#Return option
			for event in events:
				if event.type == MOUSEBUTTONDOWN:
					self.lose_music.get_sfx().fadeout(100)
					if lab_tryagain.click(event.pos):
						self.lose_music.get_sfx().fadeout(100)
						return 1
					if lab_mainmenu.click(event.pos):
						self.lose_music.get_sfx().fadeout(100)
						return 0
					
		if status == "pause":
			labs = []
			x = 150
			y = 350
			offset = 600
			lab_continue = Label("Continue", (pos[0]+x,pos[1]+y), 28, (255,255,255))
			lab_mainmenu = Label("Main Menu", (pos[0]+x+offset,pos[1]+y), 28, (255,255,255))
			labs.append(lab_continue)
			labs.append(lab_mainmenu)
			#Blit
			level.blit_all(self.screen)
			self.screen.blit(self.image, pos)
			for lab in labs:
				self.screen.blit(lab.text, lab.rect)
			#Return option
			for event in events:
				if event.type == MOUSEBUTTONDOWN:
					if lab_continue.click(event.pos): return 1
					if lab_mainmenu.click(event.pos): return 0
		
		#CODICES
		if status.startswith("codex_"):
			labs = []
			x = 450
			y = 460
			lab_back = Label("Back", (pos[0]+x,pos[1]+y), 23, (255,255,255))
			labs.append(lab_back)
			#Blit
			self.screen.blit(self.codex_bg, pos)
			try:
				self.screen.blit(self.image, pos, (0, 0, abs(int(900*float(self.all_codices[int(status[-2:])-1])/100)), 480))
				self.screen.blit(self.codex_mask, pos, (0, 0, abs(int(900*float(self.all_codices[int(status[-2:])-1])/100)), 480))
			except:
				self.screen.blit(self.image, pos, (0, 0, abs(int(900*float(self.all_codices[int(status[-1])-1])/100)), 480))
				self.screen.blit(self.codex_mask, pos, (0, 0, abs(int(900*float(self.all_codices[int(status[-1])-1])/100)), 480))
			for lab in labs:
				self.screen.blit(lab.text, lab.rect)
			#Return option
			for event in events:
				if event.type == MOUSEBUTTONDOWN:
					if lab_back.click(event.pos): return 0
				
				
		
		if status == "win":
			labs = []
			x = 300
			y = 190
			offset_x = 700
			offset_y = 30
			lab_resume = Label("Codex: "+str(int(level.Cdx.health))+"% Saved", (pos[0]+x+150, pos[1]+y), 30, (255,255,255))
			y += offset_y + 30
			lab_viewcodices = Label("View Codices", (pos[0]+x+150, pos[1]+y+150), 20, (255,255,255))
			y += offset_y + offset_y + 80
			x -= 20
			lab_mainmenu = Label("Main Menu", (pos[0]+x-150, pos[1]+y), 28, (255,255,255))
			lab_continue = Label("Continue", (pos[0]+x+offset_x-200, pos[1]+y), 28, (255,255,255))
			labs.append(lab_resume)
			labs.append(lab_viewcodices)
			labs.append(lab_mainmenu)
			labs.append(lab_continue)
			#Blit
			if self.win_music.is_playing() == False:
				self.win_music.get_sfx().play()
			level.blit_all(self.screen)
			self.screen.blit(self.image, pos)
			for lab in labs:
				self.screen.blit(lab.text, lab.rect)
			#Return option
			for event in events:
				if event.type == MOUSEBUTTONDOWN:
					if lab_mainmenu.click(event.pos):
						self.win_music.get_sfx().fadeout(100)
						self.save_codices(level.level_number, level.Cdx.health)
						return 0
					if lab_continue.click(event.pos):
						self.win_music.get_sfx().fadeout(100)
						self.save_codices(level.level_number, level.Cdx.health)
						return 1
					if lab_viewcodices.click(event.pos):
						self.win_music.get_sfx().fadeout(100)
						self.save_codices(level.level_number, level.Cdx.health)
						return 2
		
		if status == "howtoplay":
			x = 450
			y = 450
			labs = []
			
			lab_mainmenu = Label("Main Menu", (pos[0]+x, pos[1]+y), 23, (255,255,255))
			labs.append(lab_mainmenu)
			
			#Blit
			self.screen.blit(self.image, pos)
			for lab in labs:
				self.screen.blit(lab.text, lab.rect)
			
			#Return option
			for event in events:
				if event.type == MOUSEBUTTONDOWN:
					if lab_mainmenu.click(event.pos): return 0
		
		if status == "codices":
			x = 450
			y = 450
			labs = []
			lab_levels = []
			col_1 = [pos[0]+280, pos[1]+130]
			col_2 = [pos[0]+590, pos[1]+130]
			for level in range(1,6):
				lab_levels.append(Label(str(level)+". "+self.level_names[level], (col_1[0], col_1[1]), 16, (236,207,79), bool(float(self.all_codices[level - 1]))))
				col_1[1] += 40
				
			for level in range(6,11):
				lab_levels.append(Label(str(level)+". "+self.level_names[level], (col_2[0], col_2[1]), 16, (236,207,79), bool(float(self.all_codices[level - 1]))))
				col_2[1] += 40
			lab_levels.append(Label(("11. "+self.level_names[11]), (col_2[0]-col_1[0]/2, col_1[1]+20), 16, (236,207,79), bool(float(self.all_codices[10]))))
			
			lab_mainmenu = Label("Main Menu", (pos[0]+x, pos[1]+y), 23, (255,255,255))
			
			labs.append(lab_mainmenu)
			for l in lab_levels:
				labs.append(l)
			
			#Blit
			self.screen.blit(self.image, pos)
			for lab in labs:
				self.screen.blit(lab.text, lab.rect)
			#Return option
			for event in events:
				if event.type == MOUSEBUTTONDOWN:
					for l in labs:
						if l.click(event.pos): return labs.index(l)
			
		if status == "about":
			x = 100
			y = 450
			labs = []
				
			lab_mainmenu = Label("Main Menu", (pos[0]+x, pos[1]+y), 23, (255,255,255))
			labs.append(lab_mainmenu)
			
			#Blit
			self.screen.blit(self.mainscreen, pos)
			self.screen.blit(self.image, pos)
			for lab in labs:
				self.screen.blit(lab.text, lab.rect)
			#Return option
			for event in events:
				if event.type == MOUSEBUTTONDOWN:
					if lab_mainmenu.click(event.pos): return 0
			
