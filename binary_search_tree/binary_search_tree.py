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
        current = self
        # compare to the new value we want to insert
        new_node = BSTNode(value)

        # if new value < self.value
        if new_node.value < current.value:
            # IF self.left is already taken by a node
            if current.left is not None:
                # make that (left) node, call insert
                current.left.insert(new_node.value) 
            # set the left to the new node with the new value
            else:
                current.left = new_node

        # if new value >= self.value
        elif new_node.value >= current.value:
            # IF self.right is already taken by a node
            if current.right is not None:
                # make that (right) node call insert
                current.right.insert(new_node.value) 
            # set the right child to the new node with new value
            else:
                current.right = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value < target
        # found = False
        if self.value < target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            found = self.left.contains(target)
            if self.left is None:
                return False
            return found

        # if current value >= target
        elif self.value >= target:
            # check if right subtree contains target
            # if you cannot go right, return False
            found = self.right.contains(target)
            if self.right is None:
                return False
            return found

    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will always be to the right of the current node
        # if we can go right, lets find the largest number there by calling get_max on the right subtree
        max_val = self.value
        if self.right is None:
            max_val = self.value
            return max_val
        elif self.right is not None:
            if self.right.right is None:
                max_val = self.right.value
            else:
                self.right.right.get_max()
        # if we cannot go right, return the current value
        return max_val
    
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