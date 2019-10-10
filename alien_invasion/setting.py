import random

class Settings():
	"""docstring for Setting"""
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 700
		self.screen_size = (self.screen_width,self.screen_height)
		self.bg_color = (230,230,230)
		self.ship_speed = 15
		self.alien_speed = 10
		self.alien_down_speed = 20
		self.alien_direction = 1

		#子弹设置
		self.bullet_speed_factor = 5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullet_allowed = 10

	def change_back_color(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.bg_color = (r,g,b)


		