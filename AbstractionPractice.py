
from abc import ABC, abstractmethod

class animal(ABC):
    def greetings(self):
        print("Hello! I am an animal")

    @abstractmethod
    def territoryMarking(self):
        pass

class lizard(animal):
    def territoryMarking(self):
        print("This is my territory! Watch as I do pushups")







if __name__ == "__main__":
    Iggy = lizard()
    Iggy.territoryMarking()
