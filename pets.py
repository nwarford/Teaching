class Pet() :
    def __init__(self, name, species, breed, loc = "NO LOCATION"):
        self.name = name
        self.species = species
        self. breed = breed
        self.location = loc
    
    def __str__(self):
        msg = "This pet's name is " + self.name
        return msg
    
def main():
    test = Pet("Robert", "cat", "Norwegian Shorthair")
    print(test)
    
if __name__ == "__main__" :
    main()