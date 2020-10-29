#!/usr/bin/env python3

"""
File: tandem_trivia_forntend.py
----------------------
This program runs a `Tandem Trivia` game.
"""

#source: http://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=welcome%20%0ATandem%0ATrivia
from colorama import init, Fore, Style
from tandem_trivia import TriviaGame

class PrintCore():
	def __init__(self):
		pass
	
	def print_intro(self):
		print(f"""{Fore.GREEN}

		   ▄▄▄▄▀ ██      ▄   ██▄   ▄███▄   █▀▄▀█ 
		▀▀▀ █    █ █      █  █  █  █▀   ▀  █ █ █ 
		    █    █▄▄█ ██   █ █   █ ██▄▄    █ ▄ █ 
		   █     █  █ █ █  █ █  █  █▄   ▄▀ █   █ 
		  ▀         █ █  █ █ ███▀  ▀███▀      █  
		           █  █   ██                 ▀   
		          ▀                              
		   ▄▄▄▄▀ █▄▄▄▄ ▄█     ▄   ▄█ ██          
		▀▀▀ █    █  ▄▀ ██      █  ██ █ █         
		    █    █▀▀▌  ██ █     █ ██ █▄▄█        
		   █     █  █  ▐█  █    █ ▐█ █  █        
		  ▀        █    ▐   █  █   ▐    █        
		          ▀          █▐        █         
		                     ▐        ▀   
		""")
		print(f"Got a minute?\nWelcome to Tandem Trivia!\n\n{Fore.YELLOW}Choose an option to begin.{Style.RESET_ALL}\n")

	def print_game_over(self):
		print(f"""{Fore.MAGENTA}
			  _____              
			 / ___/__ ___ _  ___ 
			/ (_ / _ `/  ' \/ -_)
			\___/\_,_/_/_/_/\__/ 
			/ _ \ |/ / -_) __/   
			\___/___/\__/_/                     

			Your have earned -- points.
			Well done!
		""")
		exit()


	def print_navigation_bar(self):
		print("| [1] GET INFO | [2] START GAME | [3] CHOOSE MODE | [4] QUIT |")
		NavigationBar().navigation_bar()

class NavigationBar():
	def __init__(self):
		pass

	def print_info(self):
		init(autoreset=True)
		print(f"""{Fore.GREEN}
		Got a minute? \n
		Welcome to the TANDEM TRIVIA!

		{Fore.YELLOW}
		###########
		## TL;DR ##
		###########
		{Fore.CYAN}
		- ROUND_ONE has 10 questions.
		- ROUND_TWO has 5 questions for doubling your points or
		loosing them all.

		- Use digits to choose from multipe-choice answers.
		- Use `q` or `quit` to terminate the game at any time.
		- Use `s` or `score` to check your current score at any time.

		- GAME_MODES: RELAXED and CHALLENGE

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
		- Use `q` or `quit` to terminate the game at any time.
		- Use `s` or `score` to check your current score at any time.

		{Fore.YELLOW}
		################
		## GAME MODES ##
		################
		{Fore.CYAN}
		- RELAXED MODE: Has no timer, and you can skip any questions
		twice per game. 
		- CHALLENGE MODE: Has a timer and gives you 10 seconds
		to answer a question, does not have a possibility
		to skip questions.

		""")
		PrintCore().print_navigation_bar()

	def start_game(self):
		TriviaGame().run_game()
		PrintCore().print_game_over()

	def choose_mode(self):
		print("in_developement")
		pass

	#def play_bonus_round(self):
	#	user_input = input("Do you want to play BONUS ROUND? [Y | N] ")
	#	while True:
	#		if user_input.lower() == 'y' or user_input.lower() == 'yes':
	#			TriviaGame().run_bonus_round()
	#			PrintCore().print_game_over()
	#		if user_input.lower() == 'n' or user_input.lower() == 'no':
	#			PrintCore().print_game_over()
	#		else:
	#			user_input = input("Please, choose a valid option: [Y | N] ")

	def	navigation_bar(self):
		while True:
			user_input = input('')
			if user_input == '1':
				self.print_info()
			if user_input == '2':
				self.start_game()
			if user_input == '3':
				self.choose_mode()
			if user_input == '4' or user_input.lower() == 'q':
				exit()
			else:
				print("Please, choose a valid option:")

def main():
	PrintCore().print_intro()
	PrintCore().print_navigation_bar()

if __name__ == "__main__":
	main()
