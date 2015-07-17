age = input("how old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")

print("so you are %r years old, %r tall and %r heavy." % (age, height, weight))

print("Does asking for input work this way as well?")
answer = input()

print("You typed %r." % answer)

#Study Drills
#What does raw_input() do in python 2.7?
####Anything inside the raw_input([prompt]) is written to output leaving an opportunity for a user response.
####when enter key is pressed the input line is read in as a string and stored in the var.

#What does input() do in python 3.4?
####Anything inside the input([prompt]) is written to output leaving an opportunity for user input.
####when the enter key is pressed the input line is read in a string and stored in the var. 

print("What happens when you ask a question?")
answer2 = input()
print("The data ---> %s <--- is collected so that it can be manipulated?" % answer2)