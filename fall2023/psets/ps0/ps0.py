#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    #check if node is none
    if v == None:
        return 0
    #if not, recurse on both sides and add 
    v.size = 1 + calculate_sizes(v.left) +  calculate_sizes(v.right)
    return v.size

    pass

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)

def find_vertex(r): 
    return find_vertex_size(r, r.size)
    pass

#this helper function just retains the original number of nodes in the tree
def find_vertex_size(r, n): 
    #ensure that the node exist
    if r != None:
        if r.left == None:
            if r.right == None:
                return r #if both sides DNE and the r exists, return r
            #left side DNE, right side does
            else:
                return find_vertex_size(r.right, n) 

        #right side DNE, left side does
        elif r.right == None: 
            return find_vertex_size(r.left, n)
        
        else: #both sides exist
            #find larger of the two sides
            if r.left.size < r.right.size:
                vmax = r.right
            else:
                vmax = r.left

            #check if larger side is less than desired value
            if vmax.size <= n/2:
                return r
            else: 
                return find_vertex_size(vmax, n)
