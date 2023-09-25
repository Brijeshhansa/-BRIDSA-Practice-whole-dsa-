'''
Binary Serach Tree (BST) implimentation in python
19Aug2023
'''

#define node class
class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    # insert method in node class 
    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
    
    # get min of all keys using get_min() method
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        print('Minimum Value:',current.val)

    # get max of all keys using get_min() method
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        print('Maximum Value:',current.val)
    
    # delete method to remove any node by key
    def delete(self, val):
        if self == None:
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    # checl if node exist with key
    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)
    
    # method to print the tree in preoder
    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    # method to print the tree inorder
    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    # method to print three in post order
    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals


bst = BSTNode()
subsubmainloop = 1
while(subsubmainloop!=0):
    subsubmainloop = int(input('\n\nEnter a choice:\n1 to insert node\n2 to get minimum key value\n3 to get maximum keyvalue\n4 to delete a node with key value\n5 to check if a element exists\n6 to get tree in preorder\n7 to get tree as inorder\n8 to get tree in postorder\n9 to go to back menu\n0 to exit program'))
    if(subsubmainloop==0):
        mainloopchoice = '0'
        submainloopchoice = '0'
        print('\n\nThank you for using my software\nCopyright 2023 - brijesh')
    elif(subsubmainloop==1):
        val = int(input('\n-> Enter a number to insert in tree:\t'))
        bst.insert(val)
    elif(subsubmainloop==2):
        bst.get_min()
    elif(subsubmainloop==3):
        bst.get_max()
    elif(subsubmainloop==4):
        val = int(input('\n-> Enter a key to delete node in the tree:\t'))
        bst.delete(val)
    elif(subsubmainloop==5):
        val = int(input('\n-> Enter a key to check if it exists in the tree:\t'))
        check = bst.exists(val)
        print(check)
    elif(subsubmainloop==6):
        print(bst.preorder([]))
    elif(subsubmainloop==7):
        print(bst.inorder([]))
    elif(subsubmainloop==8):
        print(bst.postorder([]))
    elif(subsubmainloop==9):
        subsubmainloop = '0'
        print("thank you for using tree in dsa")
        break
    else:
        print('\n\nError: Invalid choice,\nplease try again and enter a valid choice\nor enter 0 to exit program.')