import sys
import pygame
from settings import Settings
from cat import Cat

def run_game():
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Cat Vs Fish")

	cat = Cat(screen)

	screen.fill(settings.background_color)
	cat.blitme()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		pygame.display.flip()

run_game()