x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

# string inside string X2
y = "Those who know %s and those who %s" % (binary,do_not)

print (x)
print (y)

#string inside string
print("I said %r" % x)

#string inside string
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w="this is the left side of ..."
e="a string with a right side."

#string + string concatenation
print(w+e)

