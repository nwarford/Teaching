try:
    x = int(input("Enter a number: "))
    y = 10/x
except ValueError: 
    print("a")
except ZeroDivisionError: 
    print("b")
except:
    print("c")
    
print(x)
print(y)