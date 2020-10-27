#!/usr/bin/env python3

import colorama
import json
import random

class PrepareData():
	def __init__(self):
		self.path_to_file = './data/Apprentice_TandemFor400_Data.json'

	def	_parse_file(self):
		with open(self.path_to_file) as f: 
  			return json.load(f) 

	def _create_options(self, data):
		for i in range(len(data)):
			data[i].setdefault('options', data[i]['incorrect'].copy())
			data[i]['options'].append(data[i]['correct'])

	def get_data(self):
		data = PrepareData()._parse_file()
		PrepareData()._create_options(data)
		return data

class TriviaGame():
	def __init__(self):
		self.questions = PrepareData().get_data()
		self.total_num_questions = len(self.questions)
		self.max_questions_round_one = 10
		self.total_score = 0
		self.options_list = []
		self.random_options_order = []

	def	generate_random_sequence(self):
		return random.sample(range(0, self.total_num_questions), self.total_num_questions)
	
	def	get_next_question(self, questions_sequence):
		return questions_sequence.pop()

	def print_options_randomly(self, next_question):
		options_count = len(self.questions[next_question]['options'])
		self.options_list = self.questions[next_question]['options']
	
		self.random_options_order = random.sample(range(0, options_count), options_count)
		for choice, position in enumerate(self.random_options_order):
			print(f"Option [{choice + 1}]: {self.options_list[position]}")

	def	prompt_user_for_input(self):
		# TO DO: check if input is int, if not error and ask again
		# check that the answer is in a correct range `options_count`
		return int(input("\nWhat do you think? "))

	def	evaluate_user_choice(self, user_choice, next_question):
		correct_answer = self.questions[next_question]['correct']
		user_answer = self.options_list[self.random_options_order[user_choice - 1]]

		if correct_answer == user_answer:
			self.total_score += 10
			print(f"\nCorrect!\n")
		else:
			print(f"Incorrect. Correct answer is {correct_answer}\n")
		print(f"Your total score is {self.total_score}.\n") 

	def	run_game(self):
		print(f"Got a minute?\n\nWelcome to TANDEM TRIVIA!\n")

		questions_sequence = self.generate_random_sequence()

		for question_count in range(0, self.max_questions_round_one):
			next_question = self.get_next_question(questions_sequence)

			print(f"\nQuestion #{question_count + 1}: {self.questions[next_question]['question']}\n")
			self.print_options_randomly(next_question)
			user_choice = self.prompt_user_for_input()
			self.evaluate_user_choice(user_choice, next_question)
		#check how many points was earned, if enougn --> well done, if not, do you want to try again? or practice makes
		# it perfect
		print(f"Round one is over. Your have earned {self.total_score} points. Well done!\n") 

def main():
	TriviaGame().run_game()

if __name__ == "__main__":
	main()