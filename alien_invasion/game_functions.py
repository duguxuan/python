import sys
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
import time

def check_keydown_events(event,ship,ai_settings,screen,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		creat_bullet(ship,ai_settings,screen,bullets)
	elif event.key == pygame.K_q:
		sys.exit()


def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_events(ai_settings,screen,ship,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship,ai_settings,screen,bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets,aliens):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	aliens.draw(screen)
	for bulet in bullets:
		bulet.draw_bullet()
	pygame.display.flip()

def check_collision(bullets,aliens):
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	#print(collisions)
	if collisions:
		for k in collisions:
			bullets.remove(k)
			aliens.remove(collisions[k])

def update_bullets(ai_settings,screen,aliens,ship,bullets):
	for i in bullets:
		i.update()
	for i in bullets.copy():
		if i.rect.bottom <= 0:
			bullets.remove(i)
	check_collision(bullets,aliens)
	if len(aliens)==0:
		bullets.empty()
		creat_fleet(ai_settings,screen,aliens,ship)


def creat_bullet(ship,ai_settings,screen,bullets):
	if len(bullets) < ai_settings.bullet_allowed:
			new_bullet = Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)

def get_number_alien_x(ai_settings,alien_width):
	aviliable_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(aviliable_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_row(ai_settings,ship_height,alien_height):
	aviliable_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(aviliable_space_y/(2*alien_height))
	return number_rows

def creat_alien(ai_settings,screen,aliens,x,y):
	alien = Alien(ai_settings,screen)
	alien.x = alien.rect.width + 2 * alien.rect.width * x 
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height*y
	aliens.add(alien)

def creat_fleet(ai_settings,screen,aliens,ship):
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	number_x = get_number_alien_x(ai_settings,alien_width)
	number_y = get_number_row(ai_settings,ship.rect.height,alien_height)

	#创建一行外星人
	for y in range(number_y):
		for x in range(number_x):
			creat_alien(ai_settings,screen,aliens,x,y)
			creat_alien(ai_settings, screen, aliens, x, y)

def update_alien(ai_settings,status,screen,ship,aliens,bullets):
	for i in aliens:
		i.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		print("Ship hit!!!")
		ship_hit(ai_settings,status,screen,ship,aliens,bullets)
	check_alien_bottom(ai_settings, status, screen, ship, aliens, bullets)

def ship_hit(ai_settings,status,screen,ship,aliens,bullets):
	aliens.empty()
	bullets.empty()
	ship.center_ship()
	update_screen(ai_settings, screen, ship, bullets, aliens)
	time.sleep(2)
	if status.ship_left>0:
		status.ship_left -= 1
		creat_fleet(ai_settings, screen, aliens, ship)
	else:
		status.game_active = False


def check_alien_bottom(ai_settings,status,screen,ship,aliens,bullets):
	screen_rect = screen.get_rect()
	for i in aliens.sprites():
		if i.rect.bottom >= screen_rect.bottom-10:
			ship_hit(ai_settings,status,screen,ship,aliens,bullets)
			break
