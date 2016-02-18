"""Implement an MVC Mastermind game for one player. This file is the controller."""

__author__ = "Ron Shafii"


from mastermind_model import * #imports all classes
from mastermind_view import *
import random



class MasterMind:


	def __init__(self):
		self.model = MasterModel()
		self.view = MasterView()
		



	def generate_goal(self):
		"""create 4 randomly generated colored pegs to establish the goal of the game."""#need to return to fix use of peg colors
		# goal = []
		# temp_list = [PlayerPeg.RED, green, blue, yellow, black, white] NEED TO FIX
		# for x in range(4):
		# 	player_peg = PlayerPeg(random.choice(MasterModel.peg_colors))
		# 	goal.append(player_peg)
		# return goal 
		pass



	def play_game(self):
		"""plays the mastermind game"""

		#Show the game rules and objectives


		#prompt the user to enter 4 colors


		#check if the user won 


			#if the user didn't win evaluate the player's peg colors against the computer_peg colors
			#if no colors match display to the user Nothing to display


				#if player colors match then evaluate if any of the player's pegs position match the computer's peg positions
				#return the appropriate position and color matches to the player

			#decrement the number of guesses left
			#display to the user the number of guesses left before they lose the game
			#if the number of guesses == 0 then display they lost the game.

			#loop back to prompt the user to enter 4 colors 


		pass


	def store_player_pegs(self):
		"""Call prompt_user to obtain player pegs. Turn prompt_user() string into a Guess object and store it in the guesses[Guess] list"""
		#
		prompt_user_results = self.view.prompt_user()

		#create a temp list
		temp_list = []

		#turn a character into a peg
		for char in prompt_user_results:
			if char == "Y":
				peg = PlayerPeg(PlayerPeg.YELLOW)
			elif char == "B":
				peg = PlayerPeg(PlayerPeg.BLUE)
			elif char == "G":
				peg = PlayerPeg(PlayerPeg.GREEN)
			elif char == "R":
				peg = PlayerPeg(PlayerPeg.RED)
			elif char == "K":
				peg = PlayerPeg(PlayerPeg.BLACK)
			elif char == "W":
				peg = PlayerPeg(PlayerPeg.WHITE)
			temp_list.append(peg)

		#create a Guess object, move the results stored in temp_list and convert them to an object then store them as a list in guesses
		temp_object = Guess() #creating an object of the Guess class
		temp_object.player_pegs = temp_list #change the temp_list to a Guess object 
		self.model.guesses.append(temp_object) #storing the objects as a list in MasterModel-guesses

		print(self.model.guesses)


		





	def check_win(self):
		"""checks to see if the player's guess (mastermind_model.Guess.player_peg) exactly matches the 
		4 computer generated pegs (mastermind_model.MasterModel.goal). """
		
		#takes the results stored from prompt_user and turns it into a True or False statement

		# check if player_peg1 == computer_peg1

		#check if player_peg2 == computer_peg2

		#check if player_peg3 == computer_peg3

		#check if player_peg4 == computer_peg4



		#if [mastermind_model.Guess.player_peg] == goal
		#	print ("You Win!")
		# if not Win then forward the info to eval_peg_color()






	def eval_peg_color():
		"""Evaluates whether the player's peg colors matches any of the computer's colors. 
		Results are stored by class Guess in the model. """

		#check if player_peg1 color matches any computer_peg color

		#check if player_peg2 color matches any computer_peg color

		#check if player_peg3 color matches any computer_peg color

		#check if player_peg4 color matches any computer_peg color
		pass

	def eval_peg_position():
		"""Evaluates whether any of the matched colors from eval_peg_color also match the 
		correct peg positions and returns a black or white peg as necessary. """

		#check if player_peg1 position is the same as computer_peg1 position

		#check if player_peg2 position is the same as computer_peg2 position

		#check if player_peg3 position is the same as computer_peg3 position

		#check if player_peg4 position is the same as computer_peg4 position



			#keypeg1 = mastermind_model.KeyPeg(KeyPeg.SMALL_BLACK)
		pass





# def test():
# 	#testing the random color generator
# 	test_object = MasterMind()
# 	temp_list = test_object.generate_goal()
# 	for peg in temp_list:
# 		print(peg.color)


# test()

