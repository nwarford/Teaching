class Thing:
    def __init__(self, a):
        self.val = a
        
    def swap(self, other):
        # temp = self.val
        print("T's value is:", self.val)
        self.val = other.val
        print("T's value is:", self.val)
        other.val = self.val
        # other.val = temp
        # return other

def main():
    t = Thing("apple")
    t2 = Thing("robot")
    t.swap(t2)
    print(t.val, t2.val)
    
if __name__ == "__main__" :
    main()