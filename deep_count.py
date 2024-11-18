def deep_count(nested) :
    """
    takes an arbitrary list and counts the number of non-list elements that appear in any list.
    """
    # Base case
    if nested == [] :
        return 0
    elif type(nested) != list :
        return 1
    else :
        # recursive call
        # if type(nested[0]) != list :
        #     return 1 + deep_count(nested[1:])
        # else :
        return deep_count(nested[0]) + deep_count(nested[1:])

print(deep_count([1,1,1,1,1])) # should be 5
print(deep_count([1,1,1,1,"1"])) # should be 5
print(deep_count([[1,2],2,[1,2]])) # should be 5
print(deep_count([1,[[],[1,2],3],3])) # should be 5