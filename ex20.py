#This statement imports sys module(library)
#from that module it activates the argv "argument variable" function?
from sys import argv

#This statment inserts the arguments given into program variables.
script, input_file = argv

#This function prints the contents of a given file.
def print_all(f):
	print(f.read())

#This function resets the point that we are reading to beginning.
def rewind(f):
	f.seek(0)

#This function labels and reads lines one at a time.
def print_a_line(line_count, f):
	print(line_count,f.readline())

#This statment initiates the file object using open() function 	
current_file = open(input_file)

print("First let's print the whole file:\n")

#This statement calls the print_all function for the file object known as current_file.
print_all(current_file)

print("Now lets rewind the file:")

#This statement calls the rewind function for the file object named "current_file"
rewind(current_file)

#The following statements call the print_a_line function that labels and prints one line at a time.
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)