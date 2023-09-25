class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

# Create an empty circular linked list
my_circular_linked_list = CircularLinkedList()

subsubloopchoice = 1
while (subsubloopchoice!=0):
    subsubloopchoice = input('Enter a choice:\n\n0 to exit\n1 Add an element to the list\n2 Display the list \n3 enter to back menu')

    if (subsubloopchoice == '1'):
        data = int(input("Enter an element to add to the list: "))
        my_circular_linked_list.append(data)
    elif(subsubloopchoice == '2'):
        my_circular_linked_list.display()
    elif(subsubloopchoice == '3'):
        subsubloopchoice = '0'
        
        print('Thank you for using my circular linked list.\n\nCopyright 2023 - brijesh')
        break
    elif(subsubloopchoice=='0'):
        mainloopchoice = '0'
        submainloopchoice = '0'
        print('Thank you for using my Software.\n\nCopyright 2023 - brijesh')
        break
    else:
        print("Invalid choice. Please try again.")
