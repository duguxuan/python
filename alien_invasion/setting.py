import random

class Settings():
	"""docstring for Setting"""
	def __init__(self):
		self.screen_width = 1000
		self.screen_height = 600
		self.screen_size = (self.screen_width,self.screen_height)
		self.bg_color = (230,230,230)
		self.ship_speed = 2
		self.ship_limit = 3
		self.alien_speed = 1
		self.alien_down_speed = 60
		self.alien_direction = 1

		#子弹设置
		self.bullet_speed_factor = 5
		self.bullet_width = 500
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullet_allowed = 10

	def change_back_color(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.bg_color = (r,g,b)


		