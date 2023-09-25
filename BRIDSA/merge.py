# MergeSort in Python with user fed data
import random

def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


data = []

i = 1
while(i!='0'):
    i = input('Enter a choice number:\n1 to insert element\n2 to perform insertion sort\n3 to print list\n0 for back menu')
    
    if(i=='0'):
        print('--- Thanks for using my Merge sort program ---\n')
    elif(i=='1'):
        x = input('Enter a number element:\t')
        if(x.isnumeric()):
            x=int(x)
            data.append(x)
        else:
            print('Error: only number is allowed')
    elif(i=='2'):
        mergeSort(data)
    elif(i=='3'):
        print(data)
    else:
        print('Error: invalid choice')