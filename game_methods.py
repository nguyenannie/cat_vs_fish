import sys
import pygame
from stone import Stone

def check_events(screen, settings, cat, stones):
	"""Respond to keypresses and mouse events"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_event(screen, settings, event, cat, stones)
			elif event.type == pygame.KEYUP:
				check_keyup_event(event, cat)

def check_keyup_event(event, cat):
	"""Response to key releases"""
	if event.key == pygame.K_RIGHT:
		cat.moving_right = False
	elif event.key == pygame.K_LEFT:
		cat.moving_left = False

def check_keydown_event(screen, settings, event, cat, stones):
	"""Response to keypresses"""
	if event.key == pygame.K_RIGHT:
		cat.moving_right = True
	elif event.key == pygame.K_LEFT:
		cat.moving_left = True
	elif event.key == pygame.K_SPACE:
		throw_stone(screen, settings, cat, stones)

def update_screen(screen, settings, cat, stones):
	"""Update images on the screen and flip to the new screen."""
	screen.fill(settings.background_color)
	cat.blitme()
	for stone in stones.sprites():
		if stone.rect.bottom <= 0:
			stones.remove(stone)
		stone.draw_stone()
	pygame.display.flip()

def update_stones(stones):
	"""Update position of stones and get rid of old stones"""
	stones.update()
	for stone in stones.sprites():
		if stone.rect.bottom <= 0:
			stones.remove(stone)
		stone.draw_stone()

def throw_stone(screen, settings, cat, stones):
	"""Throw a stone if limit is not reached yet"""
	if len(stones) < settings.stones_allowed:
			new_stone = Stone(screen, settings, cat)
			stones.add(new_stone)