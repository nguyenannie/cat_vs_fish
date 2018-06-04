import sys
import pygame
from stone import Stone
from fish import Fish

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

def update_screen(screen, settings, cat, stones, fishes):
	"""Update images on the screen and flip to the new screen."""
	screen.fill(settings.background_color)
	cat.blitme()
	fishes.draw(screen)
	for stone in stones.sprites():
		stone.draw_stone()
	pygame.display.flip()

def update_stones(stones):
	"""Update position of stones and get rid of old stones"""
	stones.update()
	for stone in stones.copy():
		if stone.rect.bottom <= 0:
			stones.remove(stone)

def throw_stone(screen, settings, cat, stones):
	"""Throw a stone if limit is not reached yet"""
	if len(stones) < settings.stones_allowed:
			new_stone = Stone(screen, settings, cat)
			stones.add(new_stone)

def create_pool(screen, settings, fishes, cat):
	"""Create a full pool of fishes"""
	fish = Fish(screen, settings)
	number_fishes_x = get_number_fishes_x(settings, fish.rect.width)
	number_rows = get_number_rows(settings, cat.rect.height, fish.rect.height)
	for row_number in range(number_rows):
		for fish_number in range(number_fishes_x):
			create_fish(screen, settings, fishes, fish_number, row_number)

def create_fish(screen, settings, fishes, fish_number, row_number):
	"""Create a fish and put it in a row"""
	fish = Fish(screen, settings)
	fish_width = fish.rect.width
	fish_height = fish.rect.height
	fish.x = fish_width + 2 * fish_width * fish_number
	fish.y = fish_height + 2 * fish_height * row_number
	fish.rect.x = fish.x
	fish.rect.y = fish.y
	fishes.add(fish)

def get_number_fishes_x(settings, fish_width):
	"""Determine the number of fishes that fit in a row"""
	available_space_x = settings.screen_width - 2 * fish_width
	return int(available_space_x / (2 * fish_width))

def get_number_rows(settings, cat_height, fish_height):
	"""Determine the number of rows of fishes that fit on the screen"""
	available_space_y = settings.screen_height - cat_height - 3 * fish_height
	return int(available_space_y / (2 * fish_height))