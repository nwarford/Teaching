import random

def animal_function(choice):
    # choice = random.randint(0,2)
    animal = ''
    if choice == 0 :
        # do something
        animal = '_/\\_/\\_0>'
    elif choice == 1 :
        # do something else
        animal = '=^..^='
    elif choice == 2 :
        # do something
        animal = '(0.0)'
        
    if choice == 1 :
        print("meow")
    return animal
    

print("Welcome to the text animal generator!")

perRunChoice = random.randint(0,2)

genAnimal = animal_function(1)
print(genAnimal)

# '_/\\_/\\_0>'
# '=^..^='
# '(0.0)'