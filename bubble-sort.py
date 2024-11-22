def bubble_sort(arr):
    numsteps = 0
  
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
              
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                # Mark that a swap has occurred
                swapped = True
                print(arr)
                numsteps += 1
                print("Number of steps:",numsteps)
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

# Source: https://www.geeksforgeeks.org/python-program-for-bubble-sort/

bubble_sort([3,2,1])