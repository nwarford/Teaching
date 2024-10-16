def change(nums):
    print("This should still be 3,2,1: ", nums)
    nums[0] = nums[0] + 1
    nums[1] = nums[1] - 1
    print("Now it should be 4, 1, 1: ", nums)
    nums = [1, 2, 3]
    print("Nums has been reassigned: ", nums)
    
def main():
    numbers = [3,2,1]
    change(numbers)
    print("Numbers got edited in the change function: ", numbers)
    
main()