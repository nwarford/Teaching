def isListType(alist, atype) :
    """
    Takes a list and a type and checks if all items of the list are that type.
    """
    if alist == [] :
        return True
    else :
        return isListType(alist[1:], atype) and (type(alist[0]) == atype)
    # if type(alist[0]) == atype :
    #     try :
    #         return isListType(alist[1:], atype)
    #     except :
    #         return True
    # else :
    #     return False
    

# print(isListType([1, 2, 3], str)) # should be false
# print(isListType([1, 2, 3], int)) # should be true
# print(isListType([1, 2, "3"], int)) # should be false
# print(isListType([], None))

def isListSameType(alist) :
    """
    Takes a list and checks if all items are the same type.
    """
    # if len(alist) <= 1 :
    #     return True
    # else :
        # if type(alist[0]) == type(alist[1]) :
        #     return isListSameType(alist[1:])
        # else :
        #     return False
        # return type(alist[0]) == isListSameType(type(alist[1:]))
        
    if alist == [] :
        return True
    else :
        # if type(alist[0]) == type(alist[-1]) :
        #     return isListSameType(alist[1:])
        # else :
        #     return False        
        return (type(alist[0]) == type(alist[-1])) and isListSameType(alist[1:])


print(isListSameType([1, 2, 3])) # should be true
print(isListSameType([1, 2, "3"])) # should be false
print(isListSameType([])) # should be true
print(isListSameType(["CSCI 150"])) # should be true
