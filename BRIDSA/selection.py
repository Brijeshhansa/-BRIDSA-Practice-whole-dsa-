# Selection sort in Python with user input
import random

def selectionSort(array, size):

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = []

i = 1
while(i!='0'):
    i = input('Enter a choice number:\n1 to go to main menu\n2 to insert element\n3 to perform insertion sort\n4 to print list\n0 for back menu')
    
    if(i=='0'):
        print('--- Thanks for using my Selection sort program ---\n')
    elif(i=='1'):
        pass
    elif(i=='2'):
        x = input('Enter a number element:\t')
        if(x.isnumeric()):
            x=int(x)
            data.append(x)
        else:
            print('Error: only number is allowed')
    elif(i=='3'):
        size = len(data)
        selectionSort(data, size)
    elif(i=='4'):
        print(data)
    else:
        print('Error: invalid choice')