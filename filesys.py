"""
Program: filesys.py   pg.183
Author: Brandon			

Provides a menu-driven tool navigating a file system and gathering information on files.
"""

import os, os.path

QUIT = '7'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7')

MENU = """1 List the current directory
2 Move up
3 Move down
4 Number of files in directory
5 Size of the directory in bytes
6 Search for a filename
7 Quit the program"""

def main():
	while True:
		print(os.getcwd())
		print(MENU)
		command = acceptCommand()
		runCommand(command)
		if command == QUIT:
			print("Have a nice day!")
			break

def acceptCommand():
	"""Inputs and returns a legitimate command number"""
	command = input("Enter a number: ")
	if command in COMMANDS:
		return command
	else: 
		print("Error: command not recognized")
		return acceptCommand()

def runCommand(command):
	"""Selects and runs a command based on the users menu choice"""
	if command == '1':
		listCurrentDir(os.getcwd())
	elif command == '2':
		moveUp()
	elif command == '3':
		moveDown(os.getcwd())
	elif command == '4':
		print("The total number of files is", countFiles(os.getcwd()))
	elif command == '5':
		print("The total number of bytes is", countBytles(os.getcwd()))
	elif command == '6':
		target = input("Enter the filename you are looking for: ")
		fileList = findFiles(target, os.getcwd())
		if not fileList: 
			print("File not found")
		else:
			for f in fileList:
				print(f)

def listCurrentDir(dirName):
	"""Prints a list of the cwd's contents."""
	lyst = os.listdir(dirName)
	for elements in lyst:
		print(element)

def moveUp():
	"""Moves up to the parent directory unless the cwd is the root"""
	os.chdir("..")

def moveDown(currentDir):
	"""Moves down to the named subdirectory if it exists."""
	newDir = input("Enter the directory name: ")
	if os.path.exists(currentDir + os.sep + newDir) and os.path.isdir(newDir):
		os.chdir(newDir)
	else:
		print("ERROR: no such name")

def countFiles(path):
	"""Returns the number of files in the cwd and all its subdirectories."""
	count = 0
	lyst = os.listdir(path)
	for element in lyst:
		if os.path.isfile(element):
			count += 1
		else:
			os.chdir(element)
			count += countFiles(os.getcwd())
			os.chdir("..")
	return count

	def countBytes(path):
		"""Returns the number of bytes in the cwd and all its subdirectories"""
		count = 0
		lyst = os.listdir(path)
		for element in lyst:
			if os.path.isfile(element):
				count += os.path.getsize(element)
			else:
				os.chdir(element)
				count += countBytes(os.getcwd())
				os.chdir("..")
			return count

def findFiles(target, path):
	"""Returns a list of the filenames thatcontai the target string in the cwd and all its subsidiaries"""
	files = []
	lyst = os.listdir(path)
	for element in lyst:
		if os.path.isfile(element):
			if target in element:
				files.append(path + os.sep + element)
			else:
				os.chdir(element)
				files.extend(findFiles(target, os.getcwd()))
				os.chdir("..")
		return files

if __name__ == "__main__":
	main()