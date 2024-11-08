class Pet() :
    def __init__(self, name, species, breed, loc = "NO LOCATION"):
        self.name = name
        self.species = species
        self. breed = breed
        self.location = loc
    
    def __str__(self):
        msg = "This pet's name is " + self.name
        return msg

class Dog(Pet) :
    def __init__(self, name, breed, loc):
        super().__init__(name, "Dog", breed, loc)
    
def main():
    # test = Pet("Robert", "cat", "Norwegian Shorthair")
    bestDog = Dog("Capo", "greyhound", "00000")
    # bestDog = Pet("Capo", "dog","greyhound", "00000")
    print(bestDog.species)
    
if __name__ == "__main__" :
    main()