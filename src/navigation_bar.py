#!/usr/bin/env python3

from colorama import init, Fore, Style
from src.print import PrintTrivia
from src.tandem_trivia import TriviaGame

class NavigationBar():
	'''
	NavigationBar() class handles user input.
	'''
	def __init__(self):
		pass

	def print_info(self):
		''' Prints information about Tandem Trivia '''
		init(autoreset=True)
		print(f"""{Fore.GREEN}
		{Fore.YELLOW}
		###########
		## TL;DR ##
		###########
		{Fore.CYAN}
		- ROUND_ONE has 10 questions.
		- ROUND_TWO is optional and has 5 questions. You will either double your score
		  from the first round or lose all the points.

		- Use digits to choose from multipe-choice answers.
		- Use `s` or `score` to check your current score at any time.
		- Use `q` or `quit` to terminate the game at any time.

		{Fore.YELLOW}
		##################
		## GENERAL INFO ##
		##################
		{Fore.CYAN}
		- ROUND_ONE consists of 10 questions;
		- ROUND_TWO is optional and consists of 5 questions. 
		  If you answer all 5 questions correctly you will double your score 
		  from the first round. Otherwise, you will lose all points.
		
		So, be wise and decide if you want to take on a challenge,
		but we all know that a little challenge goes a long way :)

		{Fore.YELLOW}
		################
		## NAVIGATION ##
		################
		{Fore.CYAN}
		- Use digits to choose from multipe-choice answers. Depending on
		  how many options you have, you can choose any option you think
		  is a correct answer, given you only choose ONE.
		- Use `s` or `score` to check your current score at any time.
		- Use `q` or `quit` to terminate the game at any time.
		""")
		self.navigation_bar()

	def start_game(self):
		''' Runs Tandem Trivia game. '''
		score = TriviaGame().run_game()
		PrintTrivia().print_game_over(score)

	def	navigation_bar(self):
		''' Processes user input. '''
		PrintTrivia().print_navigation_bar()
		while True:
			user_input = input('')
			if user_input == '1':
				self.print_info()
			if user_input == '2':
				self.start_game()
			if user_input == '3' or user_input.lower() == 'q':
				exit()
			else:
				print("Please, choose a valid option:")
				