#!/usr/bin/env python3

from src.print import PrintTrivia
from src.navigation_bar import NavigationBar

def main():
	''' Runs Tandem Trivia app'''
	PrintTrivia().print_intro()
	NavigationBar().navigation_bar()

if __name__ == "__main__":
	main()