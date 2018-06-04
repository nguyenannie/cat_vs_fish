import sys
import pygame
from settings import Settings
from cat import Cat
import game_methods as gm
from pygame.sprite import Group
from fish import Fish

def run_game():
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Cat Vs Fish")

	cat = Cat(screen, settings)
	stones = Group()
	fishes = Group()
	gm.create_pool(screen, settings, fishes, cat)

	while True:
		gm.check_events(screen, settings, cat, stones)
		gm.update_stones(stones)
		gm.update_fishes(settings, fishes)
		cat.update()
		gm.update_screen(screen, settings, cat, stones, fishes)

run_game()