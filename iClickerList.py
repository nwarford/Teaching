def new_day(slist, score):
    """
    Creates a new element with the score value (integer 0 or 1) at the most recent position of a student's iClicker data list.
    """
    slist.insert(0, score)
    # Add code to modify the list here
    return

# iClickerList = [
#     ['Michael', 1, 0, 1, 1, 1],
#     ['Emily', 1, 1, 1, 0, 0],
#     ['Noel', 1, 1, 1, 1, 1]
#     ]

iClickerDict = {
    'Michael' : [1, 0, 1, 1, 1],
    'Emily' :  [1, 1, 1, 0, 0],
    'Noel' : [1, 1, 1, 1, 1]
}

print("Unedited dictionary")
for i in iClickerDict.items() :
    print(i)

# print("Unedited list: ")
# for i in iClicker:
#     print(i)

print()

# We'll write our for loop here!
# for i in iClicker :
#     # slist.insert(1, score)
#     # iClicker[i].insert(1, 1)
#     # new_day(slist, score)
#     # print(i)
#     new_day(i, 0)

todayDict = {
    'Michael' : 1,
    'Emily' : 0,
    'Noel' : 1
}

for k in iClickerDict :
    new_day(iClickerDict[k], todayDict[k])
    
# print("Edited list:")
# for i in iClicker:
#     print(i)

print("Edited dictionary")
for i in iClickerDict.items() :
    print(i)