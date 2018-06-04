class Settings():
	"""A class to store all settings for Cat Vs Fish Game"""
	def __init__(self):
		"""Initialize the game's settings"""
		self.screen_width = 1000
		self.screen_height = 700

		self.background_color = (255, 255, 255)

		self.cats_limit = 3

		self.stone_side = 15
		self.stone_color = (0, 0, 0)

		self.stones_allowed = 3
		self.pool_drop_speed = 10
		
		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.cat_speed_factor = 1.5
		self.stone_speed_factor = 1
		self.fish_speed_factor = 5
		self.pool_direction = 1
		self.fish_point = 50

	def increase_speed(self):
		"""Increase speed settings and fish point values."""
		self.cat_speed_factor *= self.speedup_scale
		self.stone_speed_factor *= self.speedup_scale
		self.fish_speed_factor *= self.speedup_scale
		self.fish_point = int(self.fish_point * self.score_scale)
