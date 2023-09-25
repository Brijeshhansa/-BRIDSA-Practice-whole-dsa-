class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create an empty linked list
my_linked_list = LinkedList()
subsubloopchoice = 1
while (subsubloopchoice!=0):
    subsubloopchoice = input('Enter a choice:\n\n0 to exit\n1 Add an element to the list\n2 Display the list \n3 enter to back menu')
    

    if (subsubloopchoice == '1'):
        data = int(input("Enter an element to add to the list: "))
        my_linked_list.append(data)
    elif(subsubloopchoice == '2'):
        my_linked_list.display()
    elif(subsubloopchoice == '3'):
        subsubloopchoice = '0'
        break
    elif(subsubloopchoice=='0'):
        mainloopchoice = '0'
        submainloopchoice = '0'
        print('Thank you for using my Software.\n\nCopyright 2023 - brijesh')
        break
    else:
        print("Invalid choice. Please try again.")

