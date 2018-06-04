import pygame
from pygame.sprite import Sprite

class Stone(Sprite):
	"""A class to manage hooks thrown from the cat"""
	def __init__(self, screen, settings, cat):
		super().__init__()
		self.screen = screen
		self.rect = pygame.Rect(0, 0, settings.stone_side, settings.stone_side)
		self.rect.centerx = cat.rect.centerx
		self.rect.top = cat.rect.top

		self.y = float(self.rect.y)

		self.color = settings.stone_color
		self.speed_factor = settings.stone_speed_factor

	def update(self):
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_stone(self):
		pygame.draw.rect(self.screen, self.color, self.rect)



