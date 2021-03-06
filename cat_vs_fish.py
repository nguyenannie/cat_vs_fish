import sys
import pygame
from settings import Settings
from cat import Cat
import game_methods as gm
from pygame.sprite import Group
from fish import Fish
from game_stat import GameStat
from button import Button
from scoreboard import Scoreboard

def run_game():
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Cat Vs Fish")

	cat = Cat(screen, settings)
	play_button = Button(screen, settings, "Play")
	game_stats = GameStat(settings)
	scoreboard = Scoreboard(screen, settings, game_stats)
	stones = Group()
	fishes = Group()
	gm.create_pool(screen, settings, fishes, cat)

	while True:
		gm.check_events(screen, settings, cat, stones, game_stats, play_button, fishes, scoreboard)
		if game_stats.game_active:
			cat.update()
			gm.update_stones(screen, settings, stones, fishes, cat, game_stats, scoreboard)
			gm.update_fishes(screen, settings, game_stats, fishes, stones, cat, scoreboard)
		gm.update_screen(screen, settings, cat, stones, fishes, play_button, game_stats, scoreboard)

run_game()
