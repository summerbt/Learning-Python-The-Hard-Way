
def multiply(multiplier, top):
	i=multiplier
	numbers = []

	while i<= (top*multiplier):
		print(i)
		numbers.append(i)

		i+=multiplier
		print("Numbers now:", numbers)
	

	for num in numbers:
		print (num)

multiply(5,12)
