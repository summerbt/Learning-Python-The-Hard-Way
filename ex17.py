from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("copying from %s to %s" % (from_file, to_file))

#we could do these two lines on one line, how?
in_file = open(from_file)
indata = in_file.read()

print("The input is %d bytes long" % len(indata))

print("does the output file exist? %r" % exists(to_file))
print("Ready, hit return to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
out_file.close()
in_file.close()