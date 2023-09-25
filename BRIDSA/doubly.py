# Initialise the Node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.start_node = None

    # Insert Element to Empty list
    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is not empty")

    # Insert element at the end
    def InsertToEnd(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return

        n = self.start_node
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n


##### Insert at position (magic node - insert element at position)
    def insertnode(self,newnode,index):
        current = self.start_node
        count = 1
        if(index == 1):
            newnode.next = self.start_node
            self.start_node = newnode

        while current:
            if(count+1 == index):
                newnode.next = current.next
                current.next = newnode
                return
            else:
                count += 1
                current = current.next

        pass

    # Delete the elements from the start
    def DeleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None

    # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

# ### delete node of given value
    def deletenode(self,value):
        current = self.start_node
        if(current == value):
            self.head = current.next
        else:
        
            while current:
                if(current.item  == value):
                    break

                prev = current
                current = current.next

        if (current == None):
            return

        prev.next = current.next
        current = None

    # Traversing and Displaying each element of the list
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            count = 1
            while n is not None:
                print("Element ",count,': ', n.item)
                n = n.next
                count += 1
        print("\n")


# Create a new Doubly Linked List
dll = doublyLinkedList()


subsubloopchoice = 1
while(subsubloopchoice!='0'):
    subsubloopchoice = input('Enter a choice:\n\n1 for add head to doubly linked list\n2 for insert element to end \n3 for insert element at a position\n4 for delete head node\n5 for delete end node\n6 for delete node with given value as data\n7 for printing the list\n8 1toenter to back menu\n0 to exit program:\t')
    
    if(subsubloopchoice=='1'):
        x = input('Enter data to add as head:\t')
        dll.InsertToEmptyList(x)
    elif(subsubloopchoice=='2'):
        x = input('Enter data to add as element:\t')
        dll.InsertToEnd(x)
    elif(subsubloopchoice=='3'):
        x = input('Enter data to add as element:\t')
        p = input('Enter position where you want to add element:\t')
        y = Node(x)
        dll.insertnode(y,p)
    elif(subsubloopchoice=='4'):
        print('Deleting head node...')
        dll.DeleteAtStart()
        print('Head node deleted...')
    elif(subsubloopchoice=='5'):
        print('Deleting end node...')
        dll.delete_at_end()
        print('End node deleted...')
    elif(subsubloopchoice=='6'):
        x = input('Enter element to delete node:\t')
        dll.deletenode(x)
    elif(subsubloopchoice=='7'):
        print('\n\n')
        dll.Display()
    # choice to go to back menu
    elif(subsubloopchoice=='8'):
        subsubloopchoice='0'
        print('--- Thanks for using my doubly linked list program ---\n')   
    elif(subsubloopchoice=='0'):
        mainloopchoice = '0'
        submainloopchoice = '0'
        print('Thank you for using my Software.\n\nCopyright 2023 - brijesh')
   
    else:
        print('\n\n ---> Error: invalid choice, try again *** \n\n')







