#!/usr/bin/env python3

"""
File: tandem_trivia.py
----------------------
This program runs a `Tandem Trivia` game.
"""

import json
import random
from colorama import init, Fore, Style

class PrepareData():
	'''
	PrepareData() class parses a data from a given json file,
	and adds a `key : [values]` containing all multiple-choice options
	to each `question` in the data. 

	Attribute:
    	path_to_file (str): A path to file containing the data.
	'''
	def __init__(self):
		self.path_to_file = './data/Apprentice_TandemFor400_Data.json'

	def __parse_file(self):
		''' Parses json file to a list.

		Returns:
			json.load(f) (list): A list of dictionaries
				containing all `questions` and corresponding
				`correct` and `incorrect` answers.
		'''
		with open(self.path_to_file) as f: 
  			return json.load(f) 

	def __create_options(self, data):
		''' Creates and appends `options` containing
		all multiple-choice answers to each `question` in the given data.

		Attribute:
			data (list of dictionaries): A data containing `questions`,
				`correct` and `incorrect` keys.
		'''
		for i in range(len(data)):
			data[i].setdefault('options', data[i]['incorrect'].copy())
			data[i]['options'].append(data[i]['correct'])

	def get_data(self):
		''' Calls private methods to parse file and create `options`
		key with both `correct` and `incorrect` values.

		Returns:
			data (list of dictionaries): A data containing `questions`,
				`correct`, `incorrect` and `options` keys with
				corresponding values.
		'''
		data = PrepareData().__parse_file()
		PrepareData().__create_options(data)
		return data

class TriviaGame():
	'''
	TriviaGame() class implements all methods needed to run
	the `Tandem Trivia` game.
 
	Attributes:
		questions(list of dictionaries): The list of dictionaries
			containing both questions and answers to those questions.
		total_num_questions (int): A len of the questions list.
		max_questions_round_one (int): A max of questions to ask in
			round one.
		options_list (list): An empty list to be used to store
			a list of multiple-choice answers to a given question.
		options_count(int): A len of the options_list.
		random_options_order (list): An empty list to be used to
			store a list of random ints between 0 and
			len(options_list), which will define the order of
			answers to be displayed.
		total_score (int): An int that keeps track of a user's
			total score in any given time.
	'''
	def __init__(self):
		self.questions = PrepareData().get_data()
		self.total_num_questions = len(self.questions)
		self.max_questions_round_one = 10
		self.options_list = []
		self.options_count = 0
		self.random_options_order = []
		self.total_score = 0
		self.is_bonus_round = 0
		self.count_correct_answers = 0
		self.questions_sequence = []


	def __generate_random_sequence(self):
		''' Generates random sequence of ints between 0 and the
		total number of questions to define the order of questions
		to ask.

		Returns:
			(list): A list of random ints
				between 0 and len(total_num_questions),
				which defines the order of questions to ask.
		'''
		self.questions_sequence = random.sample(range(0, self.total_num_questions), \
									self.total_num_questions)
	
	def __get_next_question(self):
		''' Pops an item from the end of the given
		self.questions_sequence.

		Attribute:
			self.questions_sequence(list): A list with an 
				order of questions to ask.

		Returns:
			(int): The last element of the self.questions_sequence.
		'''
		return self.questions_sequence.pop()

	def __print_options_randomly(self, next_question):
		''' Prints, in a random order, multiple-choice answers 
		for a given question.

		Attribute:
			next_question(int): A position of a given question in
				the list of all questions.
		'''
		self.options_count = len(self.questions[next_question]['options'])
		self.options_list = self.questions[next_question]['options']
	
		self.random_options_order = \
			random.sample(range(0, self.options_count), self.options_count)
		for choice, position in enumerate(self.random_options_order):
			print(f"{Fore.CYAN}Option [{choice + 1}]: {self.options_list[position]}{Style.RESET_ALL}")

	def __prompt_user_for_input(self):
		''' Prompts a user for an input and
		checks if the input is valid. 
		'''
		user_input = input("\nWhat do you think? ")
		while True:
			if user_input.lower() == 's' or user_input.lower() == 'score':
				print(f"{Fore.MAGENTA}Your current score is {self.total_score}.")
				user_input = input("\nSo, what do you think? ")
			if user_input.lower() == 'q' or user_input.lower() == 'quit':
				exit()
			if user_input.isdigit() and \
				int(user_input) in range(1, self.options_count + 1):
					return int(user_input)
			user_input = \
				input(f"\nPlease, choose a valid option between 1 and {self.options_count}: ")
			
	def __evaluate_user_choice(self, user_choice, next_question):
		''' Evaluates a user's choice against the correct answer
		given a user's choice and position of the question in
		questions list. It also prints the outcome and user's
		current score. 

		Attribute:
			user_choice(int): A user's answer choice.
			next_question(int): A position of a given question in
				the list of all questions.
		'''
		init(autoreset=True)
		correct_answer = self.questions[next_question]['correct']
		option_position = self.random_options_order[user_choice - 1]
		user_answer = self.options_list[option_position]

		if correct_answer == user_answer:
			self.count_correct_answers += 1
			if not self.is_bonus_round:
				self.total_score += 10
			print(f"\n{Fore.GREEN}Correct!\n")
		else:
			print(f"\n{Fore.RED}Incorrect. {Fore.GREEN}Correct answer is <{correct_answer}>.\n")
		if not self.is_bonus_round:
			print(f"Your current score is {self.total_score}.\n") 

	def run_bonus_round(self):
		max_questions_bonus_round = 5
		self.is_bonus_round = 1
		self.count_correct_answers = 0
		print('Welcome to the BONUS ROUND. Good luck!')

		for bonus_question_count in range(0, max_questions_bonus_round):
			next_question = self.__get_next_question()

			print(f"\n{Fore.MAGENTA}Bonus question #{bonus_question_count + 1}: {self.questions[next_question]['question']}\n")
			self.__print_options_randomly(next_question)
			user_choice = self.__prompt_user_for_input()
			self.__evaluate_user_choice(user_choice, next_question)

		if self.count_correct_answers == max_questions_bonus_round:
			self.total_score *= 2
		else:
			self.total_score = 0
		print(f"You total score is {self.total_score}")

	def run_game(self):
		''' Runs `Tandem Trivia` game 
		'''
		print(f"\nReady for the TANDEM TRIVIA?\n")
		self.__generate_random_sequence()

		for question_count in range(0, self.max_questions_round_one):
			next_question = self.__get_next_question()

			print(f"\n{Fore.YELLOW}Question #{question_count + 1}: {self.questions[next_question]['question']}\n")
			self.__print_options_randomly(next_question)
			user_choice = self.__prompt_user_for_input()
			self.__evaluate_user_choice(user_choice, next_question)
		self.play_bonus_round()

	def play_bonus_round(self):
		user_input = input("Do you want to play BONUS ROUND? [Y | N] ")
		while True:
			if user_input.lower() == 'y' or user_input.lower() == 'yes':
				self.run_bonus_round()
				break
			if user_input.lower() == 'n' or user_input.lower() == 'no':
				break
			else:
				user_input = input("Please, choose a valid option: [Y | N] ")
