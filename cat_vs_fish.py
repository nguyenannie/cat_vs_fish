import sys
import pygame
from settings import Settings
from cat import Cat
import game_methods as gm

def run_game():
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Cat Vs Fish")

	cat = Cat(screen)

	while True:
		gm.check_events(cat)
		gm.update_screen(screen, settings, cat)

run_game()