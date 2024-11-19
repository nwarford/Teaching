class Pet() :
    petCount = 0
    def __init__(self, name, species, breed, loc = "NO LOCATION"):
        self.name = name
        self.species = species
        self.breed = breed
        self.location = loc
        Pet.petCount += 1
    
    def __str__(self):
        msg = "This pet's name is " + self.name
        return msg

class Dog(Pet) :
    numDogs = 0
    def __init__(self, name, breed, loc):
        super().__init__(name, "Dog", breed, loc)
        Dog.numDogs += 1

class Lizard(Pet) :
    def __init__(self, name, breed, loc="NO LOCATION"):
        super().__init__(name, "Lizard", breed, loc)
    
def main():
    # test = Pet("Robert", "cat", "Norwegian Shorthair", 44074)
    # print(test)
    bestDog = Dog("Capo", "greyhound", "NO LOCATION")
    print(bestDog.petCount)
    anotherDog = Dog("Daisy", "greyhound", "NO LOCATION")
    print(bestDog.petCount)
    ourLizard = Lizard("Vishal", "gecko")
    print(bestDog.petCount)
    # bestDog = Pet("Capo", "dog","greyhound", "00000")
    # print(bestDog.name)
    # print(anotherDog.name)
    
if __name__ == "__main__" :
    main()