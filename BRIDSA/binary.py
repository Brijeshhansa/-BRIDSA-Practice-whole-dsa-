def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def get_sorted_input_list():
    try:
        input_list = input("Enter a sorted list of numbers (space-separated): ").split()
        input_list = [int(x) for x in input_list]
        return input_list
    except ValueError:
        print("Invalid input. Please enter a valid list of numbers.")
        return get_sorted_input_list()

def get_target():
    try:
        target = int(input("Enter the number you want to search for: "))
        return target
    except ValueError:
        print("Invalid input. Please enter a valid target number.")
        return get_target()

def main():
    input_list = []
    while True:
        print("\nOptions:")
        print("0. to quit program")
        print("1. Insert a sorted number into the list")
        print("2. Perform binary search")
        print("3. Print the current list")
        print("4. go to back menu")

        subsubmainloop = input("Enter your choice (1/2/3/4): ")

        if subsubmainloop == '1':
            new_num = int(input("Enter the number to insert: "))
            input_list.append(new_num)
            input_list.sort()
            print(f"{new_num} has been inserted into the list.")
        elif subsubmainloop == '2':
            if not input_list:
                print("The list is empty. Please insert some numbers first.")
                continue
            target = get_target()
            index = binary_search(input_list, target)
            if index != -1:
                print(f"The target number {target} was found at index {index}.")
            else:
                print(f"The target number {target} was not found in the list.")
        elif subsubmainloop == '3':
            if not input_list:
                print("The list is empty.")
            else:
                print("Current list:", input_list)

        elif(subsubmainloop=='0'):
            mainloopchoice = '0'
            submainloopchoice = '0'
            print('--- Thanks for using my Binary search program  ---\n')
            break
        elif subsubmainloop == '4':
            subsubmainloop='0'
            print("thank u for using binary search  \n copyright  brijesh")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
