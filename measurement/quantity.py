class Quantity(object):
	def __init__(self, magnitude, unit):
		self.magnitude = magnitude
		self.unit = unit

	def is_dimensionally_consistent(self, other):
		pass