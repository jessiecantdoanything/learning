# <-- this is an octothorpe B)
# I first start the code with a message that introduces everything
print("hello world")
# here it puts a message about western sayings to continue introducing
print("howdy, yonder!")
# this puts the final message about what it's doing on the screen and excitment.
print("printing...yay!!")


# practice with math
# (starting a new sentence on the screen about counting cats)
print("I will now count my cats:")
# this does the math problem that counts our "cats"
print("cats --->", 100 - 25 * 3 % 4)

# % = moduluce operate, take two numbers, divides them idk takes the quotents TAKES A 4TH MAYBE idk
# this is to start up a new message saying our next task
print("now i will count my dogs:")
# this does a math equation that counts the dogs
print("dogs --->", 3 + 2 + 1 - 5 + 4 % 2 -1 / 4 + 6)
# this is now doing a problem where it asks us whether an equation is true or false
print("is it true that 3 + 2 < 5 - 7")
# this is the statement with the math equation telling us whether it is true or false
print(3 + 2 < 5 - 7)

# stating that i will solve another math equation
print("now i will solve another math problem")
# this is the math equation
print(4 + 6 * 9 - 2.2 )

# variables
cars = 180
space_in_a_car = 4.0
drivers = 30
passengers = 115
cars_not_driven = cars - drivers
cars_driven = cars
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven

print("there are",cars,"cars available.")
print("there are only",drivers,"drivers available.")
print("there will be",cars_not_driven,"empty cars today.")
print("we can transport",carpool_capacity,"people today.")
print("we have",passengers,"to carpool today.")
print("we need to put about",average_passengers_per_car,"in each car.")

# more variables
myName = "jessie"
myAge = 15
myHeight = 62
myEyes = "brown"
myTeeth = "white"
myHair = "short hair"

print("Let's talk about %s" % myName)
print("she's %d inches tall!" % myHeight)
print("she's has eyes and %s." % (myEyes, myHair))
print("her teeth are usually %s depending on how much chai tea she's had.")
print("if I add %d and %d, i get %d." % (myAge, myHeight, myAge + myHeight))