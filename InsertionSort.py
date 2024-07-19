################This program is written by Aida Syafiqa###############
##################Insertion Sort Algorithm in Python##################

def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array

##################################################################
#CASE 1: FIXED ARRAY SIZE WITH A LIST OF NUMBERS

def insertion_default():
    # initilizing elements of the list  
    array = [2,5,8,1,3,4,6,9,7]   
    print("\n")

    print("The list of default numbers in unsorted order= ")
    print(array)
    print("\n")

    print("The list of default numbers in sorted order= ")
    print(insertion_sort(array))

##################################################################
#CASE 2: PROMPT ARRAY SIZE WITH A LIST OF NUMBERS FROM USERS

def insertion_user():

    #Intialize an empty list
    array = []
    #Prompt user array size
    arr_size = int(input("Insert your array size= "))

    #Prompt user to enter the numbers for the array
    for i in range(0,arr_size):
        num = int(input("Insert each number for array "))
        #Adding each number into the array
        array.append(num)
    print("\n")

    print("The list of numbers you entered in unsorted order = ")
    print(array)
    print("\n")

    print("The list of numbers in sorted order = ")
    print(insertion_sort(array))

##################################################################