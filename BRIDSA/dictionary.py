a='An array is a data structure used in computer programming to store a collection of elements of the same data type. These elements, often referred to as "items" or "elements," are stored in contiguous memory locations, which means they are stored one after the other in a linear fashion. Each element in an array is accessed by its index, which is an integer value that represents the elements position in the array'
b='In the context of Data Structures and Algorithms (DSA), a "graph" is a fundamental data structure used to represent a collection of interconnected nodes or vertices. Graphs are a versatile and powerful way to model various types of relationships and connections between objects or entities. They are widely used in computer science and real-world applications for tasks such as network analysis, route planning, social network analysis, and more.'
c='A linked list is a data structure used in computer science to organize and store a collection of elements, known as nodes, where each node consists of two parts: the data or value it contains and a reference (or link) to the next node in the sequence. Linked lists provide a flexible way to store data, especially when the number of elements is unknown or can change over time.'
d='A queue is a fundamental data structure in computer science and programming that follows the principle of "first-in, first-out" (FIFO). It is used to store and manage a collection of elements, where the element that was added earliest is the first one to be removed. Queues are commonly used in scenarios where elements are processed in the order they arrive.'
e='Searching algorithms, also known as search algorithms, are a fundamental component of computer science and data structures. They are used to find the presence or location of a specific element within a collection of data, such as an array, list, or database. Searching algorithms are crucial for tasks like finding a particular item in a list, searching for a specific record in a database, or locating a particular value in a data structure.'
f='Linear search, also known as sequential search, is the simplest searching algorithm. It involves iterating through the elements of the data structure one by one until the desired element is found or until all elements have been checked. Linear search works well for small datasets but becomes inefficient for larger datasets since it has a time complexity of O(n), where "n" is the number of elements.'
g='Binary search is a more efficient searching algorithm, but it requires that the data be sorted in ascending or descending order. It works by repeatedly dividing the search interval in half until the element is found. Binary search has a time complexity of O(log n), which makes it very efficient for large datasets.'
h='Hash tables, or hash maps, are data structures that use a hash function to map keys to values. Searching in a hash table involves computing the hash code for the key and using it to locate the corresponding value. Hash table search operations have an average-case time complexity of O(1) for successful searches, making them very fast for many applications.'
i='''
Sorting is a fundamental operation in computer science and data processing, where a collection of items or data elements is arranged in a specific order, often either ascending or descending. Sorting is essential for a wide range of applications, from organizing data for efficient retrieval to facilitating search algorithms and making data more human-readable.

Here are some common sorting algorithms:

Bubble Sort: Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. Bubble sort has a time complexity of O(n^2) in the worst case.

Selection Sort: Selection sort divides the list into two parts: a sorted and an unsorted portion. It repeatedly selects the smallest (or largest) element from the unsorted portion and moves it to the sorted portion. Selection sort also has a time complexity of O(n^2).

Insertion Sort: Insertion sort builds the sorted list one element at a time. It takes an element from the unsorted portion and inserts it into its correct position in the sorted portion. It has a time complexity of O(n^2) but can be efficient for small datasets.

Merge Sort: Merge sort is a divide-and-conquer algorithm that divides the list into smaller sublists, sorts them, and then merges the sorted sublists to produce a sorted list. Merge sort has a time complexity of O(n log n) in the worst case, making it more efficient for large datasets.'
'''
j='A stack is a fundamental data structure in computer science that follows the principle of "last-in, first-out" (LIFO). It is used to store and manage a collection of elements, where elements can be added or removed only from one end of the stack, often referred to as the "top" of the stack. Stacks are commonly used in various programming and computing applications to manage function calls, track program state, and solve problems that involve a last-in, first-out ordering.'
k='In data structures and algorithms (DSA), a "tree" is a hierarchical data structure consisting of nodes connected by edges. Trees are used to represent hierarchical structures where each node has zero or more child nodes. Trees play a fundamental role in DSA and are widely used in various algorithms and applications.'
i=1
while(i!='12'):
    i=input('Enter a choice:\n0 to exit\n1 what is array?\n2 what are graphs?\n3 what is linked list?\n4 what is queue?\n5 what is searching algos?\n6 what is linesr search?\n7 what is binary search\n8 what is hash table?\n9 what is sorting and its types?\n10 what is stack?\n11 what are trees?\n12 go to back menu\n-->\t')
    
    if(i=='1'):
        print(a)
    elif(i=='2'):
        print(b)
    elif(i=='3'):
        print(c)
    elif(i=='4'):
        print(d)
    elif(i=='5'):
        print(e)
    elif(i=='6'):
        print(f)
    elif(i=='7'):
        print(g)
    elif(i=='8'):
        print(h)
    elif(i=='9'):
        print(i)
    elif(i=='10'):
        print(j)
    elif(i=='11'):
        print(k)
    elif(i=='12'):
        i=0
        print("thank you for using my dictionary menu")
        break
    elif(i== '0'):
        mainloopchoice = '0'
        submainloopchoice = '0'
        i = '0'
        
        print('Thank you for using @ BRIDSA.\n\nCopyright 2023 - brijesh')
        break
    else:
        print('error')