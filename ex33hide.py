import time
def count (timelimit):
	i=1
	numbers = []

	while i<= timelimit:
		print("%d One-thousand" % i)
		numbers.append(i)
		time.sleep(1)
		i+=1

	for num in numbers:
		print (num)

print('Wanna play hide and go seek?')
input("!?!?!")

count_time=int(input("Great, how long should I count?"))

count(count_time)
print("Ready or not here I come!")