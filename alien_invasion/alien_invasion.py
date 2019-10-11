
import pygame
import time
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group 	
from game_status import GameStatus as Gs

def run_game():
	pygame.init()
	print("start")

	ai_settings = Settings()
	screen = pygame.display.set_mode(ai_settings.screen_size)
	pygame.display.set_caption("Alien Invasion")

	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建外星人
	aliens = Group()
	gf.creat_fleet(ai_settings,screen,aliens,ship)
	status = Gs(ai_settings)

	while(True):
		gf.check_events(ai_settings,screen,ship,bullets)
		if status.game_active:
			gf.update_bullets(ai_settings,screen,aliens,ship,bullets)
			gf.update_alien(ai_settings,status,screen,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,ship,bullets,aliens)
		#time.sleep(1)




run_game()

'''
		
'''