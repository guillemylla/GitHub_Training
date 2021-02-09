from datetime import date

print("Hello world!!!")
print("Hola Mundo!!!")

print("Good morning Bob!") #added from branch a2 

print("Good morning Alice")


def sayHi(name):
	"this function says hi to people"
	print("Hi, %s, have a nice %s"%(name, today))

today = date.today()
sayHi("Guillem")
sayHi("Harsha")
sayHi("Eli")
sayHi("Frank")
