#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.locals import *

from Menu import Main_Menu
from Camera import Camera
from Camera import load_image
from Level import *
from Animate import SFX

WIDTH = 900
HEIGHT = 480

#Windows compatibility
if sys.platform == 'win32' and sys.getwindowsversion()[0] >= 5:
    os.environ['SDL_VIDEODRIVER'] = 'windib'

def play_movie(mv, surface):
	game_movies = {
	"intro":"video/intro.mpg",
	"end":"video/ending.mpg",
	}
	movie = pygame.movie.Movie(game_movies[mv])
	movie.set_display(surface, Rect((0,0),(WIDTH, HEIGHT)))
	movie.play()
	while movie.get_busy():
		pass
	movie.stop()


def main():
	#Pygame Settings
	pygame.mixer.pre_init(44100, 16, 2, 4096)
	pygame.init()
	pygame.mixer.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
	pygame.display.set_caption("Nahui Tochtli")
	
	#Game Settings
	game_menu = Main_Menu(screen)
	level_number = get_levels()
	current_level = Level(level_number)
	current_status = "mainscreen"
	pause = False
	
	#Media
	music = SFX(pygame.mixer.Sound("audio/music/nahuitochtli.wav"))
	
	
	#Main Loop
	while True:
		time=clock.tick(60)
		KEYS_PRESSED = pygame.key.get_pressed()
		EVENTS = pygame.event.get()
		
		#MAIN MENU
		if current_status == "mainscreen":
			#Play music
			if not music.is_playing():
				music.get_sfx().play(-1)
			opt = game_menu.blit_menu("mainscreen", (0,0), current_level, EVENTS, level_number)
			if opt == -1:
				current_status = "quit"
			elif opt == 0:
				current_status = "newgame"
				#Stop music
				music.get_sfx().fadeout(100)
				#Play intro
				pygame.mixer.quit()
				play_movie("intro", screen)
				pygame.mixer.init()
				#Start level
				current_level = Level()
				level_number = 1
			elif opt == 1:
				current_status = "newgame"
				current_level = Level(level_number)
				#Stop music
				music.get_sfx().fadeout(100)
			elif opt == 2:
				current_status = "codices"
			elif opt == 3:
				current_status = "howtoplay"
			elif opt == 4:
				current_status = "about"
				
		#QUIT				
		if current_status == "quit":
			save_level(level_number)
			sys.exit(0)
		
		#NEW GAME / CONTINUE
		if current_status == "newgame":
			
			if not current_level.completed():
				if pause == False:
					current_level.update(time, KEYS_PRESSED, EVENTS, screen)
					if KEYS_PRESSED[K_p]:
						pause = True
						current_level.stop_music()
				if pause == True:
					opt = game_menu.blit_menu("pause", (0,0), current_level, EVENTS, level_number)
					if opt == 0:
						current_status = "mainscreen"
						pause = False
					elif opt == 1:
						pause = False
			else:
				if current_level.victory():
					#Last level
					if level_number == 11:
						#Play ending video
						pygame.mixer.quit()
						play_movie("end", screen)
						pygame.mixer.init()
						#Return to codices
						current_status = "codices"
						level_number += 1
					#Other levels
					else:
						opt = game_menu.blit_menu("win", (0,0), current_level, EVENTS, level_number)
						if opt == 0:
							level_number += 1
							current_status = "mainscreen"
						elif opt == 2:
							level_number += 1
							current_status = "codices"
						elif opt == 1:
							if level_number < 11:
								level_number += 1
								current_level = Level(level_number)

				elif not current_level.victory():
					opt = game_menu.blit_menu("lose", (0,0), current_level, EVENTS, level_number)
					#Restart this level
					if opt == 1:
						current_level = Level(level_number)
					elif opt == 0:
						current_status = "mainscreen"
		
		#ABOUT
		if current_status == "about":
			#Play music
			if not music.is_playing():
				music.get_sfx().play(-1)
				
			opt = game_menu.blit_menu("about", (0,0), current_level, EVENTS, level_number)
			if opt == 0:
				current_status = "mainscreen"
		
		#HOW TO PLAY
		if current_status == "howtoplay":
			#Play music
			if not music.is_playing():
				music.get_sfx().play(-1)
				
			opt = game_menu.blit_menu("howtoplay", (0,0), current_level, EVENTS, level_number)
			if opt == 0:
				current_status = "mainscreen"
				
		#CODICES
		if current_status == "codices":
			#Play music
			if not music.is_playing():
				music.get_sfx().play(-1)
				
			opt = game_menu.blit_menu("codices", (0,0), current_level, EVENTS, level_number)
			if opt == 0:
				current_status = "mainscreen"
			elif opt == 1:
				current_status = "codex_1"
			elif opt == 2:
				current_status = "codex_2"
			elif opt == 3:
				current_status = "codex_3"
			elif opt == 4:
				current_status = "codex_4"
			elif opt == 5:
				current_status = "codex_5"
			elif opt == 6:
				current_status = "codex_6"
			elif opt == 7:
				current_status = "codex_7"
			elif opt == 8:
				current_status = "codex_8"
			elif opt == 9:
				current_status = "codex_9"
			elif opt == 10:
				current_status = "codex_10"
			elif opt == 11:
				current_status = "codex_11"
		
		#CODEX X
		if current_status.startswith("codex_"):
			#Play music
			if not music.is_playing():
				music.get_sfx().play(-1)
				
			opt = game_menu.blit_menu(current_status, (0,0), current_level, EVENTS, level_number)
			if opt == 0:
				current_status = "codices"
				
		#System Events
		for event in EVENTS:
			if event.type==QUIT:
				save_level(level_number)
				sys.exit(0)
		pygame.display.update()

if __name__ == '__main__':
	main()

