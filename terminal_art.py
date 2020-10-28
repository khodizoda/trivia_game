#!/usr/bin/env python3

#source: http://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=welcome%20%0ATandem%0ATrivia
from colorama import Fore, Style

class terminal_art():
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
		{Style.RESET_ALL}""")
    




		#print(f"""{Fore.GREEN}
		#	  ______                __             
		#	 /_  __/___ _____  ____/ /__  ____ ___ 
		#	  / / / __ `/ __ \/ __  / _ \/ __ `__ \/
		#	 / / / /_/ / / / / /_/ /  __/ / / / / /
		#	/_/  \__,_/_/ /_/\__,_/\___/_/ /_/ /_/ 
		#	  ______     _       _
		#	 /_  __/____(_)   __(_)___ _           
		#	  / / / ___/ / | / / / __ `/           
		#	 / / / /  / /| |/ / / /_/ /            
		#	/_/ /_/  /_/ |___/_/\__,_/            
		#{Style.RESET_ALL}""")

