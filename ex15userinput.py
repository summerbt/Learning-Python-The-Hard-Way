
#This line prints the text that then prompts for user input 
#which is stored in file_again
print ("Type a filename:")
file_again = input(">")

#This line takes the user input (now stored in file_again)
#Opens it (returning a file object) 
txt_again = open(file_again)

#This line uses the read method associated with the file object
#it returns the entire content of the file object and returns it as a string
#this string is then printed to screen
#read is a method??
print(txt_again.read())

#This way is better for collecting data from end users