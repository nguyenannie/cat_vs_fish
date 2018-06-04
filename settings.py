class Settings():
	"""A class to store all settings for Cat Vs Fish Game"""
	def __init__(self):
		"""Initialize the game's settings"""
		self.screen_width = 1000
		self.screen_height = 700

		self.background_color = (255, 255, 255)

		self.cat_speed_factor = 1.5

		self.stone_speed_factor = 1
		self.stone_side = 15
		self.stone_color = (0, 0, 0)

		self.stones_allowed = 3