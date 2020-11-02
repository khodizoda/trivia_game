
#!/usr/bin/env python3

import json

class PrepareData():
	'''
	PrepareData() class parses a data from a given json file,
	and adds a `key : [values]` containing all multiple-choice options
	to each `question` in the data. 

	Attribute:
    	path_to_file (str): A path to file containing the data.
	'''
	def __init__(self):
		self.path_to_file = '../data/Apprentice_TandemFor400_Data.json'

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
		data = self.__parse_file()
		self.__create_options(data)
		return data
