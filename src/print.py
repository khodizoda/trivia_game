#!/usr/bin/env python3

from colorama import init, Fore, Style

class PrintTrivia():
	'''
	PrintTrivia class prints info about Tandem Trivia,
	handles navigation and runs trivia game.
	'''
	def __init__(self):
		pass
	
	def print_intro(self):
		''' Prints Tandem Trivia header '''
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

	def print_game_over(self, score):
		''' Prints game over and round's total score. 
		Then terminates the program.
		
		Attribute:
			score(int): Player's total score.
		'''
		print(f"""{Fore.MAGENTA}
			  _____              
			 / ___/__ ___ _  ___ 
			/ (_ / _ `/  ' \/ -_)
			\___/\_,_/_/_/_/\__/ 
			/ _ \ |/ / -_) __/   
			\___/___/\__/_/                     

			{Fore.YELLOW}
			Your have earned {score} points.
			Well done!
		""")
		exit()

	def print_navigation_bar(self):
		''' Prints navigation bar'''
		print("| [1] GET INFO | [2] START GAME | [3] QUIT |")
