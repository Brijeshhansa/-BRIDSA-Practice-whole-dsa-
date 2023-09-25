# Stack implementation in python
'''
push()
pop()
size()
peek()
isempty()
'''
# creating a stack

s=[] # define stack with a list
maxsize = int(input('Enter max size of stack:\t')) # define max size of stack with user input
   
# add element in the stack
def add(ele):
    if(len(s)<maxsize):
        s.append(ele)
        print('Element',ele,'inserted at',len(s)-1)
    else:
        print('Warning: Stack is at its max size')

    
# remove element from the stack
def remove():
    x = s.pop()
    print('Element',x,'is deleted from the stack')

# check size of the stack
def size():
    print('Current size of stack is:',len(s))

# check head of stack
def peek():
    l = len(s)-1
    print('Element at head of stack:',s[l])

# check stack for empty
def isempty():
    if(s==[]):
        print('Stack is empty')
    else:
        print('current Stack:',s)
    
    


subsubmainloop=1
while(subsubmainloop!='0'):
    
    subsubmainloop = input('Enter a choice:\n1 to add element\n2 to delete element\n3 to check the size of the stack\n4 to check the value at head\n5 to check is the stack is empty or not\n6 to go to back menu\n0 to exit:\t')
    if(subsubmainloop=='0'):
        mainloopchoice = '0'
        submainloopchoice = '0'
        print('Thanks for using my program\nCopyright 2023 - Brijesh')
    elif(subsubmainloop=='1'):
        val = input('Enter a element to insert into the stack:\t')
        add(val)
    elif(subsubmainloop=='2'):
        remove()
    elif(subsubmainloop=='3'):
        size()
    elif(subsubmainloop=='4'):
        peek()
    elif(subsubmainloop=='5'):
        isempty()
    elif(subsubmainloop=='6'):
        subsubmainloop=='0'
        print("thank you for using stack in dsa")
        break
    else:
        print('Error: invalid choice, please try again or enter 0 to exit program')
        