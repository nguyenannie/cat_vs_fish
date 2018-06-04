import pygame.font

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

	def show_score(self):
		"""Draw score to the screen"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)