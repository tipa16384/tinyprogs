# door.py

class Door:
	def __init__(self):
		self.open = False
		self.locked = False
		self.secret = False
	def isOpen(self):
		return self.open
	def open(self):
		self.open = True
	def close(self):
		self.open = False
	def isLocked(self):
		return self.locked
	def lock(self):
		self.locked = True
	def unlock(self):
		self.locked = False
	def isSecret(self):
		return self.secret
	def reveal(self):
		self.secret = False
