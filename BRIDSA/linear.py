def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def display_list(arr):
    print("Current List:", arr)

# Initialize an empty list
num_list = []

while True:
    print("\nchoices:")
    print("0. to exit program")
    print("1. Add a number to the list")
    print("2. Search for a number in the list")
    print("3. Display the list")
    print("4. to go to back menu")

    subsubmainloop = input("Enter your choice: ")

    if subsubmainloop == '1':
        num = int(input("Enter a number to add to the list: "))
        num_list.append(num)
        print(f"{num} added to the list.")

    elif subsubmainloop == '2':
        if not num_list:
            print("The list is empty. Please add numbers first.")
        else:
            target = int(input("Enter the number to search for: "))
            result = linear_search(num_list, target)
            if result != -1:
                print(f"{target} found at index {result}")
            else:
                print(f"{target} not found in the list")

    elif subsubmainloop == '3':
        if not num_list:
            print("The list is empty.")
        else:
            display_list(num_list)

    elif(subsubmainloop=='0'):
            mainloopchoice = '0'
            submainloopchoice = '0'
            print('--- Thanks for using my Binary search program  ---\n')
            break

    elif subsubmainloop == '4':
        subsubmainloop == '0'
        print("thank you for using linear search")
        break

    else:
        print("Invalid choice. Please select a valid option.")
