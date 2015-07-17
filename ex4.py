#cars available
cars = 100

#spaces in cars available
space_in_a_car = 4.0

#drivers available
drivers = 30

#passengers needing rides
passengers = 90

#cars that will not be driven because of lack of drivers
cars_not_driven = cars - drivers

#cars that can be driven
cars_driven = drivers

#defines the capacity of the cars that can be driven today
carpool_capacity = cars_driven * space_in_a_car

#average number of passengers that should be in each car.
average_passengers_per_car = passengers/cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#Study Drills:
#vars used must be initiated and referred to exactly as they are initiated
#1. In python 2.7 use must use a floating point number in your arithmetic in order to receive floating point results.
#2. see answer 1.
#3. 