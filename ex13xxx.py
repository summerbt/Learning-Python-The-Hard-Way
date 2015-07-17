from sys import argv
script, male, female = argv
body_part = input("Part of body:")
vocalization = input("Sound someone's body can make:")


print("""%s drove his %s inside her, setting off another
shattering %s that was music to his ears.
%s was quite an instrument to play, 
so finely tuned,
and if %s touched her right, 
%s made the most glorious sounds.""" % (male, body_part, vocalization, female, male, female ))