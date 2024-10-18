goalNumber = int(input("What's your goal number? ")) 

# We're going to square 2 until we exceed the goal number
# We want to know the closest power of 2 above our goal number
startingNumber = 1
while (startingNumber < goalNumber) :
    startingNumber *= 2
    print("Current startingNumber:",startingNumber)
        
print("Answer:",startingNumber)