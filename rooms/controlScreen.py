# controlScreen.py

from gamescreen import GameScreen

class ControlScreen(GameScreen):
	def __init__(self,master,bounds):
		print "ControlScreen init"
		GameScreen.__init__(self,master,bounds)

