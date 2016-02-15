"""Implement an MVC Mastermind game for one player.
This file is the model."""

__author__ = "Ron Shafii"


class Mastermodel:
	"""determines #of guesses, computer generated goal, and history of player's guesses"""

	def __init__(self):
		self.guess_num = None
		self.goal = []
		self.guesses = [Guess]



class Guess:
	"""stores history of player pegs and key pegs"""

	def __init__(self):
		self.player_peg = []
		self.key_peg = []




class Player_Peg:
	"""define the 6 colored pegs used by the player and randomly generated by the computer"""

	#globals inside the player_peg class
	RED = "red"
	BLUE = "blue"
	GREEN = "green"
	YELLOW = "yellow"
	BLACK = "black"
	WHITE = "white"


	def __init__(self, color):
		"""store the color of the peg"""
		self.color = color





class Key_Peg:
	"""define the key peg"""

	#globals inside the key_peg class
	BLACK = "black"
	WHITE = "white"


	def __init__(self, color):
		"""store the color of the peg"""
		self.color = ""