'''
Project: BRIDSA
Description: A program to demonstrate the implementation of Data Structure and Algorithms with Python language
Date: 12 sept 2023
Author: Brijesh
'''

# outer loop
mainloopchoice=1
while(mainloopchoice!='0'):
    # outer loop menu / main menu
    mainloopchoice = input('Enter a choice:\n0 to quit program\n1 to get HELP\n2 to check DSA Dictionary\n3 to enter Arrays Data Structure menu\n4 to enter LinkedLists DS menu\n5 to enter Queue DS Menu\n6 to enter Stack DS menu\n7 to enter Tree DS menu\n8 to enter Graph DS menu\n9 to enter Search Algo menu\n10 to enter Sort Algo menu\n11 to enter Greedy Algo menu\n12 to enter Asymptotic Notation menu:\n-->\t')
    
    # choice to exit program
    if(mainloopchoice=='0'):
        print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - Brijesh ***\n')
    
    # choice for help
    elif(mainloopchoice=='1'):
        import sys
        sys.path.insert(0, './help')

        submainloopchoice=1
        print('\n** Welcome to help Menu for BRIDSA **')
        while(submainloopchoice!='0'):
            
            submainloopchoice = input('Enter a choice:\n0 to exit program\n1 to go to help\n2 to go to Main Menu\n-->\t')
            
            if(submainloopchoice=='0'):
                mainloopchoice='0'
                print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - brijesh ***\n')
            elif(submainloopchoice=='1'):
                print('\n|| Welcome to help program ||\n YOU CAN PERFORM THESE OPERATIONS IN THIS APPLICATION')
                import hel
            elif(submainloopchoice=='2'):
                submainloopchoice = '0'
                print('\n\n*** Thank you for using my help @ BRIDSA ***\n')
            # invalid choice handling
            else:
                print('Error: invalid choice, try again')
            
    # choice for dictionary
    elif(mainloopchoice=='2'):
        import sys
        sys.path.insert(0, './dict')

        submainloopchoice=1
        print('\n** Welcome to dictionary Menu for BRIDSA **')
        while(submainloopchoice!='0'):
            
            submainloopchoice = input('Enter a choice:\n0 to exit program\n1 to go to dictionary\n2 to go to Main Menu\n-->\t')
            
            if(submainloopchoice=='0'):
                mainloopchoice='0'
                print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - brijesh ***\n')
            elif(submainloopchoice=='1'):
                print('\n|| Welcome to dictionary program ||')
                import dictionary
            elif(submainloopchoice=='2'):
                submainloopchoice = '0'
                print('\n\n*** Thank you for using my dictionary @ BRIDSA ***\n')
            # invalid choice handling
            else:
                print('Error: invalid choice, try again')
        pass
        
    # choice for Array Data Structure menu
    elif(mainloopchoice=='3'):
        import sys
        sys.path.insert(0, './array')

        submainloopchoice=1
        print('\n** Welcome to array Menu for BRIDSA **')
        while(submainloopchoice!='0'):
            
            submainloopchoice = input('Enter a choice:\n0 to exit program\n1 to go to array\n2 to go to Main Menu\n-->\t')
            
            if(submainloopchoice=='0'):
                mainloopchoice='0'
                print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - brijesh ***\n')
            elif(submainloopchoice=='1'):
                print('\n|| Welcome to array program ||')
                import arr
            elif(submainloopchoice=='2'):
                submainloopchoice = '0'
                print('\n\n*** Thank you for using my array @ BRIDSA ***\n')
            # invalid choice handling
            else:
                print('Error: invalid choice, try again')
        pass
    # choice for LinkedLists Data Structure menu
    elif(mainloopchoice=='4'):
        import sys
        sys.path.insert(0, './linkedlist')

        submainloopchoice=1
        print('\n** Welcome to linkedlist Algorithms Menu for BRIDSA **')
        while(submainloopchoice!='0'):
            
            submainloopchoice = input('Enter a choice:\n0 to exit program\n1 to print help\n2 to go to Main Menu\n3 for singly linkedlist\n4 for doubly linkedlist\n5 for circular linkedlist\n6 for back menu\n-->\t')
            
            if(submainloopchoice=='0'):
                mainloopchoice='0'
                print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - brijesh ***\n')
            elif(submainloopchoice=='1'):
                print('HELP MODULE IMPORT HERE')
            elif(submainloopchoice=='2'):
                submainloopchoice='0'
                pass
            # option for singly linkedlist
            elif(submainloopchoice=='3'):
                print('\n|| Welcome to singly linkedlist program ||')
                # importing the program as module
                import singly
            
            # option for doubly linkedlist
            elif(submainloopchoice=='4'):
                print('\n|| Welcome to doubly linkedlist program ||')
                # importing the program as module
                import doubly

            # option for circular linkedlist
            elif(submainloopchoice=='5'):
                print('\n|| Welcome to circular linkedlist program ||')
                # importing the program as module
                import circular
           
            # back menu
            elif(submainloopchoice=='6'):
                submainloopchoice = '0'
                print('\n\n*** Thank you for using Sorting Programs @ BRIDSA ***\n')
            # invalid choice handling
            else:
                print('Error: invalid choice, try again')

        pass
    # choice for Queue Data Structure menu
    elif(mainloopchoice=='5'):
        import sys
        sys.path.insert(0, './queue')

        submainloopchoice=1
        print('\n** Welcome to queue Menu for BRIDSA **')
        while(submainloopchoice!='0'):
            
            submainloopchoice = input('Enter a choice:\n0 to exit program\n1 to go to queue\n2 to go to Main Menu\n-->\t')
            
            if(submainloopchoice=='0'):
                mainloopchoice='0'
                print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - brijesh ***\n')
            elif(submainloopchoice=='1'):
                print('\n|| Welcome to queue program ||')
                import que
            elif(submainloopchoice=='2'):
                submainloopchoice = '0'
                print('\n\n*** Thank you for using my queue @ BRIDSA ***\n')
            # invalid choice handling
            else:
                print('Error: invalid choice, try again')
            pass
    # choice for Stack Data Structure menu
    elif(mainloopchoice=='6'):
        import sys
        sys.path.insert(0, './stack')

        submainloopchoice=1
        print('\n** Welcome to stack Menu for BRIDSA **')
        while(submainloopchoice!='0'):
            
            submainloopchoice = input('Enter a choice:\n0 to exit program\n1 to go to stack menu\n2 to go to Main Menu\n-->\t')
            
            if(submainloopchoice=='0'):
                mainloopchoice='0'
                print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - brijesh ***\n')
            elif(submainloopchoice=='1'):
                print('\n|| Welcome to stack program ||')
                import stac
            elif(submainloopchoice=='2'):
                submainloopchoice = '0'
                print('\n\n*** Thank you for using my stack @ BRIDSA ***\n')
            # invalid choice handling
            else:
                print('Error: invalid choice, try again')

        pass
    # choice for Tree Data Structure menu
    elif(mainloopchoice=='7'):
       
        import sys
        sys.path.insert(0, './tree')

        submainloopchoice=1
        print('\n** Welcome to tree Menu for BRIDSA **')
        while(submainloopchoice!='0'):
            
            submainloopchoice = input('Enter a choice:\n0 to exit program\n1 to go to tree menu\n2 to go to Main Menu\n-->\t')
            
            if(submainloopchoice=='0'):
                mainloopchoice='0'
                print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - brijesh ***\n')
            elif(submainloopchoice=='1'):
                print('\n|| Welcome to tree program ||')
                import tre
            elif(submainloopchoice=='2'):
                submainloopchoice = '0'
                print('\n\n*** Thank you for using my tree @ BRIDSA ***\n')
            # invalid choice handling
            else:
                print('Error: invalid choice, try again')

        pass
    # choice for Graph Data Structure menu
    elif(mainloopchoice=='8'):
        import sys
        sys.path.insert(0, './graph')

        submainloopchoice=1
        print('\n** Welcome to graph Menu for BRIDSA **')
        while(submainloopchoice!='0'):
            
            submainloopchoice = input('Enter a choice:\n0 to exit program\n1 to go to graph menu\n2 to go to Main Menu\n-->\t')
            
            if(submainloopchoice=='0'):
                mainloopchoice='0'
                print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - brijesh ***\n')
            elif(submainloopchoice=='1'):
                print('\n|| Welcome to graph program ||')
                import grap
            elif(submainloopchoice=='2'):
                submainloopchoice = '0'
                print('\n\n*** Thank you for using my graphs @ BRIDSA ***\n')
            # invalid choice handling
            else:
                print('Error: invalid choice, try again')

        pass
    # choice for Search Algorithm menu
    elif(mainloopchoice=='9'):
        import sys
        sys.path.insert(0, './search')

        submainloopchoice=1
        print('\n** Welcome to search Algorithms Menu for BRIDSA **')
        while(submainloopchoice!='0'):
            
            submainloopchoice = input('Enter a choice:\n0 to exit program\n1 to print help\n2 to go to Main Menu\n3 for linear search\n4 for binary search\n5 for back menu\n-->\t')
            
            if(submainloopchoice=='0'):
                mainloopchoice='0'
                print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - brijesh ***\n')
            elif(submainloopchoice=='1'):
                print('HELP MODULE IMPORT HERE')
            elif(submainloopchoice=='2'):
                submainloopchoice='0'
                pass
            # option for linear search
            elif(submainloopchoice=='3'):
                print('\n|| Welcome to linear search program ||')
                # importing the program as module
                import linear
            
            # option for binary search
            elif(submainloopchoice=='4'):
                print('\n|| Welcome to binary search program ||')
                # importing the program as module
                import binary

            # back menu
            elif(submainloopchoice=='5'):
                submainloopchoice = '0'
                print('\n\n*** Thank you for using searching Programs @ BRIDSA ***\n')
            # invalid choice handling
            else:
                print('Error: invalid choice, try again')

        pass
    # choice for Sort Algorithm menu
    elif(mainloopchoice=='10'):
        # importing sys
        import sys
        # adding program subfolder to the system path
        sys.path.insert(0, './sorting')

        submainloopchoice=1
        print('\n** Welcome to Sorting Algorithms Menu for BRIDSA **')
        while(submainloopchoice!='0'):
            
            submainloopchoice = input('Enter a choice:\n0 to exit program\n1 to print help\n2 to go to Main Menu\n3 for Bubble Sort\n4 for Insertion Sort\n5 for Merge Sort\n6 for Selection Sort\n7 for back menu\n-->\t')
            
            if(submainloopchoice=='0'):
                mainloopchoice='0'
                print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - Sahil ***\n')
            elif(submainloopchoice=='1'):
                print('HELP MODULE IMPORT HERE')
            elif(submainloopchoice=='2'):
                submainloopchoice='0'
                pass
            # option for bubble sort
            elif(submainloopchoice=='3'):
                print('\n|| Welcome to Bubble Sort program ||')
                # importing the program as module
                subsubloopchoice = '1'
                import bubble
            
            # option for insertion sort
            elif(submainloopchoice=='4'):
                print('\n|| Welcome to Insertion Sort program ||')
                # importing the program as module
                import insertion

            # option for merge sort
            elif(submainloopchoice=='5'):
                print('\n|| Welcome to Merge Sort program ||')
                # importing the program as module
                import merge

            # option for selection sort
            elif(submainloopchoice=='6'):
                print('\n|| Welcome to Selection Sort program ||')
                # importing the program as module
                import selection
            # back menu
            elif(submainloopchoice=='7'):
                submainloopchoice = '0'
                print('\n\n*** Thank you for using Sorting Programs @ BRIDSA ***\n')
            # invalid choice handling
            else:
                print('Error: invalid choice, try again')
        
        pass
    # choice for Greedy Algorithm menu
    elif(mainloopchoice=='11'):
        import sys
        sys.path.insert(0, './greedy')

        submainloopchoice=1
        print('\n** Welcome to greedy Algorithms Menu for BRIDSA **')
        while(submainloopchoice!='0'):
            
            submainloopchoice = input('Enter a choice:\n0 to exit program\n1 to print help\n2 to go to Main Menu\n3 for krushkal algos\n4 for prims algo\n5 for back menu\n-->\t')
            
            if(submainloopchoice=='0'):
                mainloopchoice='0'
                print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - brijesh ***\n')
            elif(submainloopchoice=='1'):
                print('HELP MODULE IMPORT HERE')
            elif(submainloopchoice=='2'):
                submainloopchoice='0'
                pass
            # option for linear search
            elif(submainloopchoice=='3'):
                print('\n|| Welcome to krushkal algo program ||')
                # importing the program as module
                import krushkal
            
            # option for binary search
            elif(submainloopchoice=='4'):
                print('\n|| Welcome to prims algo program ||')
                # importing the program as module
                import prim

            # back menu
            elif(submainloopchoice=='5'):
                submainloopchoice = '0'
                print('\n\n*** Thank you for using greedy algorithm Programs @ BRIDSA ***\n')
            # invalid choice handling
            else:
                print('Error: invalid choice, try again')
        pass
    # choice for Asymtotic Notation menu
    elif(mainloopchoice=='12'):
        import sys
        sys.path.insert(0, './asymptotic')

        submainloopchoice=1
        print('\n** Welcome to asymptotic notation Menu for BRIDSA **')
        while(submainloopchoice!='0'):
            
            submainloopchoice = input('Enter a choice:\n0 to exit program\n1 to see asymptotic notations\n2 to go to Main Menu\n-->\t')
            
            if(submainloopchoice=='0'):
                mainloopchoice='0'
                print('\n\n*** Thank you for using BRIDSA***\n***copyright 2023 - brijesh ***\n')
            elif(submainloopchoice=='1'):
                print('\n|| Welcome to asymptotic notations ||')
                import asymp
            elif(submainloopchoice=='2'):
                submainloopchoice = '0'
                print('\n\n*** Thank you for using my asymptotic notations @ BRIDSA ***\n')
            # invalid choice handling
            else:
                print('Error: invalid choice, try again')
        pass
    # Error handling for invalid choice
    else:
        print('\n\n***Error: invalid choice***')

