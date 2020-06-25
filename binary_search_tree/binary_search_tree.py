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
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)
            

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = []
        queue.append(node)
        while len(queue) > 0:
            first_node = queue.pop(0)
            print(first_node.value)
            if first_node.left:
                queue.append(first_node.left)
            if first_node.right:
                queue.append(first_node.right)
        return queue


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)
        while len(stack) > 0:
            last_node = stack.pop()
            print(last_node.value)
            if last_node.left:
                stack.append(last_node.left)
            if last_node.right:
                stack.append(last_node.right)
        return stack

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):

        print(self.value)
        if self.left:
            self.left.pre_order_dft(node)
        if self.right:
            self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(node)
        if self.right:
            self.right.post_order_dft(node)
        print(self.value)
