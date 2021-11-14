# target.py

from object import Object
from gamevars import *

class Target(Object):
	def __init__(self):
		Object.__init__(self)
		self.otype = O_TARGET
		self.visible = 0
		
		self.setImageName('target.png')
