
class ProtectedClass():
    def __init__(self):
        self._protectedExample = "This is a protected variable!"

TankyTank = ProtectedClass()


class PrivateClass():
    def __init__(self):
        self.__privateExample = "This is a private method!! No outsiders can access me!"

    def accessPrivate(self):
        print(self.__privateExample)

SneakySneak = PrivateClass()




if __name__ == "__main__":
    print("Protection and Private Testing!\n")
    #Protection Testing
    print("Let's see if TankyTank can access a protected variable..\n")
    print(TankyTank._protectedExample)
    print("Success! Since ._protectedExample is only protected, it can still be accessed outside the class.\n")

    #Private Testing
    print("Now let's see if SneakySneak can access a private variable...\n")
    #print(SneakySneak.__privateExample) #This is commented out since it would throw an error to the interpreter
    print("Nope! We have to use a method that's part of the class to access it. ")
    SneakySneak.accessPrivate()
    print("Success! We have accessed the private variable by using a method associated with the class!")

