def reading_d20(dice_roll) :
    """
    Gives a message depending on the dice roll.
    Input: dice roll
    Output: nothing
    """
    
    if dice_roll >= 10 and dice_roll < 20 :
        print("Good")
    elif dice_roll == 20 :
        print("Extra good! Critical hit!")
    elif dice_roll == 1 :
        print("Super extra bad.")
    else :
        print("Bad")
        
reading_d20(17)
reading_d20(2)
reading_d20(1)
reading_d20(20)