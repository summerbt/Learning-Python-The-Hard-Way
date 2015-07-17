#this statement imports sys module (library) 
#and from that module (library) activate the argv "argument variable"
from sys import argv

#This statement inserts the arguments given into program variables.
script, filename = argv

#This line opens the file called (filename) 
#and returns a File Object to txt which is now an object
txt = open(filename)

#This line prints the file name that was given as an argument
print("Here's your file %r:" % filename)

#This line reads the content of the file (property?)
#and returns it as a string
#then prints the string to the screen.
print (txt.read())

#this way is better if you are collecting data from a program??
