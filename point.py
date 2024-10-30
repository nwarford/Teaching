class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
    def __add__(self, p2) :
        newx = self.x + p2.x
        newy = self.y + p2.y
        return Point(newx, newy)  


p1 = Point(3,4)
p2 = Point(1, 1)
pTest = Point(1, 1)
# p = Point(self, 3, 4)
# p = self.Point(3, 4)
print(p1)
print(p2)
print("Then we add")
addedPoint = p1 + p2
print(addedPoint)
print("Originals")
print(p1)
print(p2)

print(pTest == p2)