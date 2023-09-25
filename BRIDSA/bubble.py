# Optimized Bubble sort in Python using user fed data

def bubbleSort(array):

  # loop through each element of array
  for i in range(len(array)):

    # keep track of swapping
    swapped = False

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
          if array[j] > array[j + 1]:

            # swapping occurs if elements
            # are not in the intended order
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp

            swapped = True

    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:
        break

data = []

subsubloopchoice = 1
while(subsubloopchoice!='0'):
    subsubloopchoice = input('Enter a choice number:\n1 to insert element\n2 to perform bubble sort\n3 to print list\n4 for back menu\n0 to exit program')
    # choice to exit program
    if(subsubloopchoice=='0'):
        mainloopchoice = '0'
        submainloopchoice = '0'
        print('--- Thanks for using my Bubble sort program ---\n')
    
    # choice to insert element
    elif(subsubloopchoice=='1'):
        x = input('Enter a number element:\t')
        if(x.isnumeric()):
            x=int(x)
            data.append(x)
        else:
            print('Error: only number is allowed')
    
    # choice to sort elements
    elif(subsubloopchoice=='2'):
        bubbleSort(data)

    # choice to print data
    elif(subsubloopchoice=='3'):
        print(data)

    # choice to go to back menu
    elif(subsubloopchoice=='4'):
        subsubloopchoice='0'
        print('--- Thanks for using my Bubble sort program ---\n')
    else:
        print('Error: invalid choice')