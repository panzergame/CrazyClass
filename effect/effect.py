class Effect:
	def __init__(self, position, life):
		self.position = position
		self.life = life

	def render(self, screen):
		pass

	def update_time(self):
		self.life -= 1
		return (self.life >= 0)
