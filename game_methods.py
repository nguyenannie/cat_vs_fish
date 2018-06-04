import sys
import pygame

def check_events(cat):
	"""Respond to keypresses and mouse events"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_event(event, cat)
			elif event.type == pygame.KEYUP:
				check_keyup_event(event, cat)

def check_keyup_event(event, cat):
	"""Response to key releases"""
	if event.key == pygame.K_RIGHT:
		cat.moving_right = False
	elif event.key == pygame.K_LEFT:
		cat.moving_left = False

def check_keydown_event(event, cat):
	"""Response to keypresses"""
	if event.key == pygame.K_RIGHT:
		cat.moving_right = True
	elif event.key == pygame.K_LEFT:
		cat.moving_left = True

def update_screen(screen, settings, cat):
	"""Update images on the screen and flip to the new screen."""
	screen.fill(settings.background_color)
	cat.blitme()
	pygame.display.flip()