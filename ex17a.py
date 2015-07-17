from sys import argv
from os.path import exists

script, from_file, to_file = argv

#we could do these two lines on one line, how?
in_file = open(from_file); indata = in_file.read()

out_file = open(to_file, 'w'); out_file.write(indata)

out_file.close()
in_file.close()

in_file = open(from_file)
out_file = open(to_file)

print("Alright, all done.")
print("%s File:" % from_file)
print(in_file.read())
print("%s File:" % to_file)
print(out_file.read())

out_file.close()
in_file.close()