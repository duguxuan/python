import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
	def __init__(self,ai_settings,screen):
		super().__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.edege_left = self.screen_rect.left
		self.edege_right = self.screen_rect.right
		self.ai_settings = ai_settings
		self.dirction = self.ai_settings.alien_direction

		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = self.rect.x

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def check_edge(self):
		if self.rect.right > self.edege_right or self.rect.left < self.edege_left:
			self.rect.y += self.ai_settings.alien_down_speed
			self.dirction *= -1

	def change_dir(self):
		self.rect.y += self.ai_settings.alien_down_speed
		self.ai_settings.alien_direction *= -1
		print("the direction is {0}\n".format(self.ai_settings.alien_direction))


	def update(self):
		self.check_edge()
		self.x += self.ai_settings.alien_speed * self.dirction
		self.rect.x = self.x
		#print(self.rect.left,self.rect.right)

	