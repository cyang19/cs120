class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind-left_size-1)
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''

    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.size += 1
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.size += 1
            self.right.insert(key)
        return self
    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        # Your code goes here
        if direction == "L":
            if child_side == "R" and self.right.right != None:
                sizetotal = self.right.size
                A = self.right.left
                B = self.right.right.left
                C = self.right.right.right

                if C == None: 
                    sizec = 0
                else:
                    sizec = C.size

                x = self.right
                y = self.right.right

                self.right = y
                y.left = x
                x.right = B

                self.right.size = sizetotal
                self.right.left.size = sizetotal - sizec - 1
                return self

            if child_side == "L" and self.left.right != None:
                sizetotal = self.left.size
                A = self.left.left
                B = self.left.right.left
                C = self.left.right.right

                if C == None: 
                    sizec = 0
                else:
                    sizec = C.size
                
                x = self.left 
                y = self.left.right 

                self.left = y
                y.left = x
                x.right = B

                self.left.size = sizetotal
                self.left.left.size = sizetotal - sizec - 1
                return self

        else:
            if child_side == "R" and self.right.left != None:
                sizetotal = self.right.size 
                A = self.right.left.left
                B = self.right.left.right
                C = self.right.right

                if A == None: 
                    sizea = 0
                else:
                    sizea = A.size
                
                x = self.right
                y = self.right.left

                self.right = y
                y.right = x
                x.left = B

                self.right.size = sizetotal
                self.right.right.size = sizetotal - sizea - 1

                return self

            if child_side == "L" and self.left.left != None:
                sizetotal = self.left.size 
                A = self.left.left.left
                B = self.left.left.right
                C = self.left.right

                if A == None: 
                    sizea = 0
                else:
                    sizea = A.size
                
                x = self.left
                y = self.left.left

                self.left = y
                y.right = x
                x.left = B

                self.left.size = sizetotal
                self.left.right.size = sizetotal - sizea - 1

                return self



    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self