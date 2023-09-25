# Initialize an empty list to store the array
my_array = []

while True:
    print("\nOptions:")
    print("0. to exit program")
    print("1. Add an element")
    print("2. Remove an element")
    print("3. Traverse the array")
    print("4. go to back menu")

    choice = input("Enter your choice: ")

    if choice == '1':
        element = int(input("Enter the element to add: "))
        my_array.append(element)
        print(f"Element {element} added to the array.")

    elif choice == '2':
        if len(my_array) == 0:
            print("The array is empty. Nothing to remove.")
        else:
            element = int(input("Enter the element to remove: "))
            if element in my_array:
                my_array.remove(element)
                print(f"Element {element} removed from the array.")
            else:
                print(f"Element {element} not found in the array.")

    elif choice == '3':
        if len(my_array) == 0:
            print("The array is empty.")
        else:
            print("Array elements:")
            for element in my_array:
                print(element, end=' ')
            print()

    elif choice == '4':
        choice='0'
        
        print("***Thank you for using array in dsa @ BRIDSA***")
        break
    elif (choice=='0'):
        mainloopchoice = '0'
        submainloopchoice = '0'
        print('--- Thanks for using my array program ---\n')
    
    else:
        print("Invalid choice. Please choose a valid option.")
