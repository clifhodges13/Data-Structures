"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)    
        cur_val = self.value
        # compare to the new value we want to insert

        if value < cur_val:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        # if new value < self.value
        # if value < cur_val:
        #     # IF self.left is already taken by a node
        #     if self.left is not None:
        #         # make that (left) node, call insert
        #         self.left.insert(value) 
        #     # set the left to the new node with the new value
        #     else:
        #         self.left = new_node

        # # if new value >= self.value
        # elif value >= cur_val:
        #     # IF self.right is already taken by a node
        #     if self.right is not None:
        #         # make that (right) node call insert
        #         self.right.insert(value) 
        #     # set the right child to the new node with new value
        #     else:
        #         self.right = new_node



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            found = self.left.contains(target)

        elif self.value <= target:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            max_val = self.value
            return max_val
        elif self.right is not None:
            if self.right.right is None:
                max_val = self.right.value
                return max_val
            else:
                return self.right.get_max()
    
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on the current value fn(self.value)
        fn(self.value)
        # if you can go left, call for_each on the left tree
        if self.left is not None:
            self.left.for_each(fn)
        # if you can go right, call for_each on the right tree
        if self.right is not None:
            self.right.for_each(fn)  

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


new_bst = BSTNode(10)
new_bst.insert(2)
new_bst.insert(12)
new_bst.insert(4)
new_bst.insert(17)
new_bst.insert(7)

print('--- contains --- ',new_bst.contains(2))