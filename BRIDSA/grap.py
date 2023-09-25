'''
Program to implement Graph (Non-linear Data Structure) in Python
Date: 2Sept2023
Author: Brijesh
Place: Jammu
'''

# class to create graph object and for creating methods to implement important graph elements like Vertex or Edge
class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def __iter__(self):
        return iter(self.vertices.values())


# vertex class to handle vertex related logic such as placement and verification, etc
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
 
g = Graph()
        
subsubmainloop = 1
while(subsubmainloop!=0):
    subsubmainloop = int(input('\nEnter a choice:\n0 to quit program\n1 to add Vertex\n2 to add Edge\n3 to display graph:\n4 to go to back menu\n-->\t'))
    
    # choice to exit program
    if(subsubmainloop==0):
        mainloopchoice = '0'
        submainloopchoice = '0'
        print('\n\n***Thank you for using my software***\n***copyright 2023 - Brijesh***')
    # choice to add vertex / node to the graph
    elif(subsubmainloop==1):
        key = input('Enter key value:\t')
        if key not in g:
            g.add_vertex(key)
        else:
            print('Vertex already exists.')
    # choice to connect two vertex with a edge
    elif(subsubmainloop==2):
        src = input('Enter source value:\t')
        dest = input('Enter destination value:\t')
        wt = input('Enter weight value:\t')
        
        if src not in g:
            print('Vertex {} does not exist.'.format(src))
        elif dest not in g:
            print('Vertex {} does not exist.'.format(dest))
        else:
            if not g.does_edge_exist(src, dest):
                if(wt.isnumeric()):
                    g.add_edge(src, dest, wt)
                else:
                        g.add_edge(src, dest)
            else:
                print('Edge already exists.')
    # print current graph
    elif(subsubmainloop==3):
        print('Vertices: ', end='')
        for v in g:
            print(v.get_key(), end=' ')
        print()
 
        print('Edges: ')
        for v in g:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))
        print()
    # to go to back menu
    elif(subsubmainloop==4):
        subsubmainloop='0'
        print("***Thank you for using graph in dsa @ BRIDSA***")
        break
        
    else:
        print('\n\n***Error: invalid choice***')


