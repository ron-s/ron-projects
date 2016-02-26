"""Implement an MVC Mastermind game for one player.
This file is the view."""

#The view doesn't know the contoller or model exist. Ex: gets a phone call, can answer but doesnt know where the phone call came from

__author__ = "Ron Shafii and Sarah Fellows"

import re
from mastermind_controller import *
from mastermind_view import *

class MasterView:


	def show_rules(self):
		"""Displays the rules of Mastermind to the player. """
		#Edit these rules to go more indepth  

		print("Welcome to Mastermind!")

		print("Object of the Game\n")
		print("The computer picks a sequence of 4 pegs, each one being one of any of six colors:\n")
		print("red, green, blue, yellow, black, and white.")
		print("The object of the game is to guess the exact positions of the colors in the -\n")
		print("sequence in as few guesses as possible. After each guess, the computer -\n")
		print("gives you a score of exact and partial matches. A black peg indicates an exact -\n")
		print("match, a white peg a partial match (right color, wrong position)\n\n")

		print("Rules")
		print("1. The sequence can contain pegs of colors: (Y)ellow, (B)lue, (G)reen, (W)hite, blac(K), and (R)ed.\n")
		print("2. A color can be used any number of times in the sequence.\n")
		print("3. Each guess must consist of 4 peg colors - no blank space are allowed.\n")
		print("4. You are must guess the computer's sequence within 10 guesses, otherwise you lose the game.\n\n")



	def prompt_user(self):
		"""Prompts the user to choose 4 colored pegs."""
		#ask the user pick 4 colors in a sequence of their choice

		#getting the player's input
		entree = input("Please select the four colors in the sequence of your choice. Remember, your color choices are (Y)ellow, (B)lue, (G)reen, (W)hite, blac(K), and (R)ed.")

		#if the player doesn't enter 4 characters
		while len(entree) != 4:
			entree = input("I do not understand your color selection. Please only enter 4 characters.")

		processed = re.fullmatch('^[YBGWKR]{4}$', entree.upper())

		if processed == None:

			print("I do not understand your color selection. Remember your color choices are: (Y)ellow, (B)lue, (G)reen, (W)hite, blac(K), and (R)ed")

		#elif do something else if they input more than 4 choices 	

		else:
			return processed.group(0)

		#return the selected user colors to the controller 


	def win(self):
		"""Displays to the player "They Won!" """
		#if check_win is True  
		#once check_win has determined they won, we show them:
		print("Congratulations! You guessed the correct peg colors and positions! You won!")

		#Maybe display key pegs?

	def lose(self):
		"""Displays to the player "Sorry, You Lose." """
		#This function has not been incorporated into the game yet. It is currently hard coded in the play_game function in the controller.

		#if guess_num reaches 10 guesses display game over
		#print ("Sorry, you didn't guess the correct peg colors or positions in 10 guesses. You loose!")



	def show_board(self, guesses):
		"""display the entire history of the player's pegs and key pegs from the stored guesses"""
		#for future task we need to display the choices horizonally as well as return they key pegs in the same line. 
		#Add ascii art 
		
		#displays the colors and position of the player's current and previous guesses 
		#as well as the key pegs based on the player's guess
		for guess in guesses:

			print("Here is all your guesses.")

			for item in guess.player_pegs:
				print(item)

			for item in guess.key_pegs:
				print(item)
			#{} and key pegs {}\n".format(guess.player_pegs, guess.key_pegs))

