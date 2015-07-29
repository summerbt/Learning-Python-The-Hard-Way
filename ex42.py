## Animal is-a object
class Animal(object):

	actions = []

	def __init__(self, name):
		self.name = name
		self.actions = ['eat','poop']

	def add_action(self, action):
		self.actions.append(action)
	
## Dog is-a Animal.
class Dog(Animal):
	def fetch(self):
		print('%s, Go Fetch!' % self.name)


## Cat is-a Animal
class Cat(Animal):
	def prowl(self):
		print('%s is on the prowl' % self.name)

## Person is-a object
class Person(object):

	def __init__(self, name):
		##Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is a person
class Employee(Person):

	def __init__(self, name, salary):
		## ?? what is this strange magic?
		super(Employee, self).__init__(name)
		## employee has-a salary
		self.salary = salary

##Fish is-a Animal
class Fish(Animal):
	def swim(self):
		print('%s is going for a swim!')

##Salmon is-a fish
class Salmon(Fish):
	pass

##Haliobut is-a Fish
class Halibut(Fish):
	pass

##rover is-an instance of a dog object
rover = Dog("Rover")
rover.add_action("Sit")
rover.add_action("Stay")
print(rover.name)
print(rover.actions)
rover.fetch()
##satan is-an instance of a cat object
satan = Cat("Satan")
satan.add_action("purr")
satan.add_action("knock things over")
print(satan.name)
print(satan.actions)
satan.prowl()
##mary is-an instance of a Person of a person object
mary = Person("Mary")
print(mary.name)

##mary has-a pet "Satan"
mary.pet = satan
print(mary.pet.name)

##frank is an instance of a employee object.
frank = Employee("Frank", 120000)
print(frank.name)
print(frank.salary)

##Frank has a pet
frank.pet = rover
print(frank.pet.name)

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()