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

		self.drop_down_mode = False

		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the fish at its current position"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.drop_down_mode:
			self.rect.y += 20
		else:
			self.x += self.settings.fish_speed_factor * self.settings.pool_direction
			self.rect.x = self.x

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def drop_down(self):
		self.rect.y += 20

		