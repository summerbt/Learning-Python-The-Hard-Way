#Study Drill ex39a
import hashmap

#create a mapping of state abbreviation
states = hashmap.new()
hashmap.set(states, "Wisconsin", "WI")
hashmap.set(states, "Michigan", "MI")
hashmap.set(states, "Illinois", "IL")

#create a basic set of states and some cities
cities = hashmap.new()
hashmap.set(cities, "WI", "Milwaukee")
hashmap.set(cities, "MI", "Detroit")
hashmap.set(cities, "IL", "Chicago")

#cities printing
print("-"*10)
for i in states:
	if i:
		for k, v in i:
			v
			print ("%s, %s" % (hashmap.get(cities, v), v))