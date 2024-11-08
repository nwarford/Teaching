class Token:
    count = 0
    def __init__(self,x):
        self.x = x + 1
        Token.count = Token.count + 1
        
t1 = Token(3)
print(t1.count, Token.count)
t2 = Token(2)
print(t2.x, t2.count, Token.count)
t3 = Token(1)
print(t2.x, t2.count, Token.count)