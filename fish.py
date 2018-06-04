import pygame
from pygame.sprite import Sprite

class Fish(Sprite):
	"""A class to represent a single fish"""
	def __init__(self, screen, settings):
		"""Initialize the fish and set its starting position"""
		super().__init__()
		self.screen = screen
		self.settings = settings

		self.image = pygame.image.load("images/fish.bmp")
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the fish at its current position"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		self.x += self.settings.fish_speed_factor * self.settings.pool_direction
		self.rect.x = self.x

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

		