
import pygame
import time
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group 	


def run_game():
	pygame.init()
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

	while(True):
		gf.check_events(ai_settings,screen,ship,bullets)
		gf.update_bullets(bullets)
		gf.update_alien(aliens)
		gf.update_screen(ai_settings,screen,ship,bullets,aliens)




run_game()

'''
		
'''