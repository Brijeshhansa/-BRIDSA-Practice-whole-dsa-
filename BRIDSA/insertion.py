# Implementing insertion sort with user fed data

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key

data = []

i = 1
while(i!='0'):
    i = input('Enter a choice number:\n1 to insert element\n2 to perform insertion sort\n3 to print list\n0 for back menu')
    
    if(i=='0'):
        print('--- Thanks for using my Insertion sort program ---\n')
    elif(i=='1'):
        x = input('Enter a number element:\t')
        if(x.isnumeric()):
            x=int(x)
            data.append(x)
        else:
            print('Error: only number is allowed')
    elif(i=='2'):
        insertionSort(data)
    elif(i=='3'):
        print(data)
    else:
        print('Error: invalid choice')