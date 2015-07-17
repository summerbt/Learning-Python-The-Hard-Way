#this statement imports sys module (library) 
#and from that module (library) activate the argv "argument variable"
from sys import argv

#This statement inserts the arguments given into program variables.
script, filename = argv

#This line opens the file called (filename) 
#and returns a File Object to txt
txt = open(filename)

#This line prints the file name that was given as an argument
print("Here's your file %r:" % filename)

#This line reads the content of the file (property?)
#and returns it as a string
#then prints the string to the screen.
print (txt.read())

#This line prints the text that then prompts for user input 
#which is stored in file_again
print ("Type the filename again:")
file_again = input(">")

#This line takes the user input (now stored in file_again)
#Opens it (returning a file object) 
txt_again = open(file_again)

#This line uses the read method associated with the file object
#it returns the entire content of the file object and returns it as a string
#this string is then printed to screen
#read is a method??
print(txt_again.read())