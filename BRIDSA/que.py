'''
Linear queue with user input

'''

queue = []

def addque(x):
    queue.append(x)

def delque():
    queue.pop(0)

def printque():
    print(queue)


subsubmainloop = 1
while(subsubmainloop!=0):
    mainloopchoice = '0'
    submainloopchoice = '0'
    subsubmainloop = int(input('Enter a Choice:\n\n0 to exit:\n1 to add element to Queue\n2 to Delete element from the queue\n3 to print the Queue\n4 to go to back menu\t'))
    
    if(subsubmainloop==0):
        print('Thank you for using my software\n\ncopyright 2023 - Brijesh')
    elif(subsubmainloop==1):
        x = input('Enter value to add to queue:\t')
        addque(x)
    elif(subsubmainloop==2):
        delque()
    elif(subsubmainloop==3):
        printque()
    elif(subsubmainloop==4):
        subsubmainloop=='0'
        print("thank you for using queue")
        break
    else:
        print('Error: invalid input, please try again or enter 0 to exit')