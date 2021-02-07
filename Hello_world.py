from datetime import date


print("Hello Bob!!!")
print("Hello, I am your  new branch!")

today = date.today()
print("Today's date:", today)


def sayHI(name):
        "This function says Hi to people"
        print("Hi, %s, have a nice %s" % (name, today))


sayHI("Bob")
sayHI("Alice")

