class GameStat(object):
	"""Track statistics for Cat Vs. Fish Game"""
	def __init__(self, settings):
		"""Initialize statistics"""
		self.settings = settings
		self.game_active = False
		self.high_score = 0
		self.reset_stats()
	
	def reset_stats(self):
		self.score = 0
		self.cats_left = self.settings.cats_limit
