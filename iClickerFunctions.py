def cloneDict() :
    newDict = {}
    for k in iClicker.items() :
        newDict[k[0]] = k[1]
    return newDict

def remove_day(iClicker) :
    """
    Remove the most recent day.
    """
    for k in iClicker.keys() :
        # iClicker[k].pop(0)
        iClicker[k] = iClicker[k][1:]
    return

def remove_day2(name) :
    iClicker[name].pop()
    return 

def hitman_2016() :
    name = input("Who do you want to off? ")
    try :
        del iClicker[name]
    except :
        print("Not a valid student")
    return

iClicker = {
    'Adam' : [1, 0, 1, 1, 0 , 1],
    'Michael' : [1, 0, 1, 1, 1],
    'Emily' :  [1, 1, 1, 0, 0],
    'Noel' : [1, 1, 1, 1, 1]
}

# testDict = cloneDict()
# print(testDict)

# remove_day(iClicker)
# remove_day2('Adam')
print(iClicker)
hitman_2016()
print(iClicker)