##############This program is written by Aida Syafiqa##############
##################Bubble Sort Algorithm in Python##################

from BubbleSort import *

##################################################################
#CASE 1: FIXED ARRAY SIZE WITH A LIST OF NUMBERS

def fixed_arr():
    # initilizing elements of the list  
    array = [2,5,8,1,3,4,6,9,7]   
    print("The list of numbers in sorted order = \n")
    print(bubble_sort(array))

##################################################################
#CASE 2: PROMPT ARRAY SIZE WITH A LIST OF NUMBERS FROM USERS

def user_arr():

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
    print(bubble_sort(array))

##################################################################
#MAIN PROGRAM: GIVE OPTIONS FOR USER TO CHOOSE

prog_opt = input("Pick the options below= \n1. Sort numbers using a fixed array\n2. Sort numbers using your array\n")
if prog_opt == '1':
    fixed_arr()
elif prog_opt == '2':
    user_arr()
else:
    print("Number inserted is invalid")