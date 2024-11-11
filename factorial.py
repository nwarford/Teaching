def factorial_recursive(n) :
    if n == 1 :
        return 1
    else :
        return n * factorial_recursive(n-1)
    
def factorial_iterative(n) :
    fac = 1
    for i in range():
        fac = fac * i
    return fac

def factorial_shortcut(n) :
    return n * factorial_shortcut(n-1)

def factorial_skip(n) :
    if n == 1 or n == 0 :
        return 1
    else :
        return n * (n-1) * factorial_skip(n-2)

print(factorial_skip(6))