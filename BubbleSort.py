##############This program is written by Aida Syafiqa##############
##################Bubble Sort Algorithm in Python##################

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        print(i)
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its lower position value. With each
        # iteration for j, the portion of the array that you look at
        # becomes lesser because the remaining items have already
        # been sorted in previous loop. hence, minus i. 
        # minus 'i' = minus previous sorted numbers in the list
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # lower position value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array