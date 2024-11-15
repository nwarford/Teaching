def len_r(alist) :
    if alist == [] :
        return 0
    else:
        return len_r(alist[1:]) + 1
    
# print(len_r(["Oscar", "Harper", "Alisha", "Nat", "Aimee", "Oscar"]))

def sum_r(nums) :
    if nums == [] :
        return 0
    else :
        return sum_r(nums[1:]) + nums[0]
    
# print(sum_r([1, 7, 18]))
# print(sum_r([]))

def count_tags(post):
    if post == "" :
        return 0
    else :
        # achar = "#"
        # if achar == "#" :
        if post[0] == "#" :
            return count_tags(post[1:]) + 1
        else :
            return count_tags(post[1:]) + 0

print(count_tags("CSCI 150 is the #greatest #blessed #yolo #theprofessorisold####"))