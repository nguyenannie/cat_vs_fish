import sys
import pygame
from stone import Stone
from fish import Fish
from time import sleep

def check_events(screen, settings, cat, stones, stats, play_button, fishes, scoreboard):
	"""Respond to keypresses and mouse events"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_event(screen, settings, event, cat, stones)
			elif event.type == pygame.KEYUP:
				check_keyup_event(event, cat)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				check_play_button(screen, settings, stats, fishes, stones, cat, play_button, mouse_x, mouse_y, scoreboard)

def check_play_button(screen, settings, stats, fishes, stones, cat, play_button, mouse_x, mouse_y, scoreboard):
	"""Start a new game when the player click play"""
	play_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if play_clicked and not stats.game_active:
		settings.initialize_dynamic_settings()
		stats.reset_stats()
		pygame.mouse.set_visible(False)
		stats.game_active = True

		fishes.empty()
		stones.empty()

		scoreboard.prep_score()
		scoreboard.prep_high_score()
		scoreboard.prep_level()
		scoreboard.prep_cats()

		create_pool(screen, settings, fishes, cat)
		cat.center_cat()

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

def update_screen(screen, settings, cat, stones, fishes, play_button, stats, scoreboard):
	"""Update images on the screen and flip to the new screen."""
	screen.fill(settings.background_color)
	cat.blitme()
	fishes.draw(screen)
	scoreboard.show_score()
	for stone in stones.sprites():
		stone.draw_stone()
	if not stats.game_active:
		play_button.draw_button()
	pygame.display.flip()

def update_stones(screen, settings, stones, fishes, cat, stats, scoreboard):
	"""Update position of stones and get rid of old stones"""
	stones.update()
	for stone in stones.copy():
		if stone.rect.bottom <= 0:
			stones.remove(stone)
	check_stone_fish_collisions(screen, settings, fishes, stones, cat, stats, scoreboard)

def check_stone_fish_collisions(screen, settings, fishes, stones, cat, stats, scoreboard):
	"""Respond to stone-fish collisions."""
	colissions = pygame.sprite.groupcollide(stones, fishes, True, False)
	if colissions:
		for fishes in colissions.values():
			for fish in fishes:
					fish.drop_down_mode = True
	if len(fishes) == 0:
		stones.empty()
		create_pool(screen, settings, fishes, cat)
		settings.increase_speed()
		stats.level += 1
		scoreboard.prep_level()

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
			create_fish(screen, settings, fishes, fish_number, row_number, cat)

def create_fish(screen, settings, fishes, fish_number, row_number, cat):
	"""Create a fish and put it in a row"""
	fish = Fish(screen, settings)
	fish_width = fish.rect.width
	fish_height = fish.rect.height
	fish.x = fish_width + 2 * fish_width * fish_number
	fish.y = fish_height + 2 * fish_height * row_number + cat.rect.height
	fish.rect.x = fish.x
	fish.rect.y = fish.y
	fishes.add(fish)

def get_number_fishes_x(settings, fish_width):
	"""Determine the number of fishes that fit in a row"""
	available_space_x = settings.screen_width - 2 * fish_width
	return int(available_space_x / (2 * fish_width))

def get_number_rows(settings, cat_height, fish_height):
	"""Determine the number of rows of fishes that fit on the screen"""
	available_space_y = settings.screen_height - 2 * cat_height - 3 * fish_height
	return int(available_space_y / (2 * fish_height))

def update_fishes(screen, settings, stats, fishes, stones, cat, scoreboard):
	"""Check if the pool is at an edge and then update the positions of all fishes in the pool"""
	check_pool_edges(settings, fishes)
	fishes.update()
	cat_fishes_colissions = pygame.sprite.spritecollide(cat, fishes, True)
	if cat_fishes_colissions:
		for fish in cat_fishes_colissions:
			stats.score += settings.fish_point
			scoreboard.prep_score()
		check_high_score(stats, scoreboard)

	check_fish_bottom(screen, settings, stats, fishes, stones, cat, scoreboard)

def check_pool_edges(settings, fishes):
	"""Respond corespondingly if any fishes have reached an edge."""
	for fish in fishes.sprites():
		if fish.check_edges():
			change_pool_direction(settings, fishes)
			break

def change_pool_direction(settings, fishes):
	"""Drop the entire pool and change the pool's direction"""
	for fish in fishes.sprites():
		fish.rect.y += settings.pool_drop_speed
	settings.pool_direction *= -1

def lose_life(screen, settings, stats, fishes, stones, cat, scoreboard):
	"""Respond to cat losing one life"""
	if stats.cats_left > 0:
		stats.cats_left -= 1
		scoreboard.prep_cats()
	else:
		stats.game_active = False
		pygame.mouse.set_visible(False)

	# fishes.empty()
	stones.empty()

	# create_pool(screen, settings, fishes, cat)
	cat.center_cat()

	sleep(0.5)

def check_fish_bottom(screen, settings, stats, fishes, stones, cat, scoreboard):
	"""Check if any fishes have reached the bottom of the screen"""
	screen_rect = screen.get_rect()

	for fish in fishes.sprites():
		if fish.rect.bottom >= screen_rect.bottom:
			lose_life(screen, settings, stats, fishes, stones, cat, scoreboard)
			break

def check_high_score(stats, scoreboard):
	"""Check to see if there's a new high score"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		scoreboard.prep_high_score()



