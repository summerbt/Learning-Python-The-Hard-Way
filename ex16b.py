from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'r+')

print ("Truncation the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print("I'm going to write these to the file.")

target.write("%s \n%s \n%s" % (line1, line2, line3))

print("And finally, we close it.")
target.close()

print("Now we can open you file to read it:")
target=open(filename)
print("%s reads:" % filename)
print(target.read())