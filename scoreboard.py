import pygame.font
from pygame.sprite import Group
from cat import Cat

class Scoreboard(object):
	"""A class to report scoring information"""
	def __init__(self, screen, settings, stats):
		"""Initialize scorekeeping attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.stats = stats

		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_cats()

	def prep_score(self):
		"""Turn score into a rendered image"""
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.settings.background_color)

		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.background_color)

		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.right = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		"""Turn the level into a rendered image"""
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.background_color)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_cats(self):
		self.cats = Group()
		for cat_number in range(self.stats.cats_left):
			cat = Cat(self.screen, self.settings)
			cat.rect.x = 10 + cat_number * cat.rect.width
			cat.rect.y = 10
			self.cats.add(cat)

	def show_score(self):
		"""Draw score and cat to the screen"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.cats.draw(self.screen)

