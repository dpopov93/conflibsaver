#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Configuration saver library, easy create, 
edit and using library for your program
setting manipulation

Author: Denis Popov
E-mail: d.popov93@mail.ru
Created: 30.11.2017
Version: 0.2

'''

import os
from pathlib import Path

class conflibsaver:
	def __init__(self, conf_file_path, display_messages=False):
		### Main variables ###
		self.data_string = None
		self.data = None
		self.conf_file_name = None
		self.conf_path = None
		self.display_messages = display_messages
		self.conf_file_path = self.install_file_path(conf_file_path)
		
		if os.path.exists(self.conf_file_path):
			self.read_file()
		else:
			self.create_file()
	
	def __del__(self):
		"""Destructor save data to config file"""
		self.save_data()
				
			
	
	def read_file(self):
		"""Reads file, recording to self.data_string.
		
		Returns:
		True -- successful reading configuration file
		False -- unsuccessful file read
		
		"""
		try:
			with open(self.conf_file_path, 'r') as f:
				self.data_string = f.read().split()
				self.data = {
					string.split('=')[0]: string.split('=')[1]
					for string in self.data_string
				}
		except IndexError as e:
			self.dbg(str(e) + ": Can\'t to parse config file. Created new")
			self.create_file()
			return False
		except FileNotFoundError as e:
			self.dbg(str(e) + ": Config file not found. Created new")
			self.create_file()
			return False
		else:
			self.dbg("Parameters in file not founded")
			if len(self.data_string) < 1: return False
		finally:
			return True
	
	def create_file(self):
		"""Create configuration file
		
		Returns:
		True -- successful creating configuration file
		False -- unable to create configuration file
		
		"""
		try:
			open(self.conf_file_path, 'w').close()
			return True
		except FileNotFoundError:
			return self.create_path_to_file()
		except PermissionError as e:
			self.dbg(str(e) + ": unable to create config file, need root permissions")
			return False

	def create_path_to_file(self):
		"""Create path to file
		
		Returns:
		True -- successful creating dir
		False -- unable to create dir
		
		"""
		try:
			os.makedirs(Path(self.conf_file_path).parent)
			return self.create_file()
		except FileExistsError as e:
			self.dbg(str(e) + ": unable to create config dir. Please, validate folder path")
			return False
	
	def install_file_path(self, conf_file_path):
		"""Validate and saves to configuration file name and path of file
		
		Keyword arguments:
		conf_file_path -- string of file location
		
		Returns:
		Valid string of file path
		"""
		conf_file_path = os.path.expanduser(conf_file_path)
		
		self.conf_file_name = Path(conf_file_path).name
		self.conf_path = Path(conf_file_path).parent
		
		return conf_file_path

	def param_count(self):
		"""Return count of parameters in config file
		
		Returns:
		0 -- if parameters in file not founded
		n > 0 -- parameter count
		"""
		if self.data != None:
			return len(self.data)
		else:
			return 0
	
	def set_param(self, param_name, param_value):
		"""Set parameter value by name
		
		Keyword arguments:
		param_name -- Parameter name
		param_value -- Parameter value
		
		Returns:
		True -- successful parameter setting
		False -- unsuccessful parameter setting
		"""
		try:
			self.data[str(param_name)] = str(param_value)
			return True
		except:
			return False
			
	
	def get_param(self, param_name):
		"""Return value of parameter by name
		
		Keyword arguments:
		param_name -- parameter's name in string
		
		Returns:
		Value -- if parameter by name is exists
		None -- if parameter is not founded
		"""
		try:
			return self.data[param_name]
		except KeyError as e:
			self.dbg(str(e) + ": Param \"" + param_name + "\" is not founded")
			return None
		except NoneType as e:
			self.dbg(str(e) + ": Param \"" + param_name + "\" is not founded")
			return None
	
	def has_param(self, param_name):
		"""Check for an existing parameter
		
		Keyword arguments:
		param_name -- parameter's name in string
		
		Returns:
		True -- if parameter by name is exists
		False -- if parameter is not founded
		"""
		if param_name in self.data:
			return True
		else:
			return False
	
	def save_data(self):
		"""Saves data to file
		
		Returns:
		True -- writing is successful
		False -- data is not writted
		"""
		if self.param_count() == False:
			self.dbg("Nothing to writing")
			return False
			
		try:
			with open(self.conf_file_path, 'w') as f:
				f.write(self.data_to_string(self.data))
		except FileNotFoundError as e:
			self.dbg(str(e) + ": unable to write data to file")
			return False
		except PermissionError as e:
			self.dbg(str(e) + ": unable to write data to file, need root permissions")
			return False
		else:
			return True
	
	def data_to_string(self, data):
		"""Converts data in one line (syntax conflib file)
		
		Keyword argument:
		data -- dictionary of params with values
		
		Returns:
		String -- converted dictionary to one line
		"""
		return '\n'.join([f'{key}={value}' for key, value in data.items()])
	
	def get_filename(self):
		"""Returns name of config file
		
		Returns:
		String -- name of config file
		"""
		return self.conf_file_name
	
	def get_path(self):
		"""Returns path of config file
		
		Returns:
		String -- name of config file's path
		"""
		return self.conf_path

	def dbg(self, text=""):
		"""Display output of errors if display messages is on
		
		Keyword arguments:
		text -- string message for display
		"""
		if self.display_messages: print(text)
