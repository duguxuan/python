import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
	def __init__(self,ai_settings,screen):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = self.rect.x

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def check_edge(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			self.rect.right = screen_rect.right - self.rect.width
			print("the screen right:{},the alien right:{}".format(screen_rect.right,self.rect.right))
			return True
		elif self.rect.left <= 0:
			print(2)
			return True
		else:
			return False

	def change_dir(self):
		self.rect.y += self.ai_settings.alien_down_speed
		self.ai_settings.alien_direction *= -1
		print("the direction is {0}\n".format(self.ai_settings.alien_direction))


	def update(self):
		change = self.check_edge()
		if change == True:
			print("change")
			self.change_dir()
		self.x += self.ai_settings.alien_speed * self.ai_settings.alien_direction
		self.rect.x = self.x

	