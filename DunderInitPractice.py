
class Dog:
    animalType = "dog"
    animalNoise = "Woof"

    def __init__(self, name, legs, color):
        self.name = name
        self.legs = legs
        self.color = color

    def greetings(self):
        msg = ("Hello! {} is a {} that goes {}! They have {} legs and is a {} color.".format(self.name, self.animalType, self.animalNoise, self.legs, self.color))
        return msg



class Westie(Dog):
    breed = "Westie"

"""
Zoey = Dog("Zoey", 4, "golden")

print(Zoey.animalType)
print (Zoey.greetings())
"""

Woofers = Westie("Woofers", 4, "Grey");
print(Woofers.breed)
print(Woofers.greetings())
