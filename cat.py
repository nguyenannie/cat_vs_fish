import pygame

class Cat():
	"""A class to manage the cat"""
	def __init__(self, screen, settings):
		"""Initialize the cat and set its starting position"""
		self.screen = screen
		self.settings = settings

		self.image = pygame.image.load("images/cat.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.moving_right = False
		self.moving_left = False

		self.center = float(self.rect.centerx)

	def blitme(self):
		"""Draw the cat at its current position"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Update the cat position based on the movement flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.settings.cat_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.settings.cat_speed_factor
		self.rect.centerx = self.center
