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
        if value < self.value:  # Check if the new nodes value is less than the current value
            if self.left is None:  # go left
                self.left = BSTNode(value)  # repeat search
            else:
                self.left.insert(value)  # insert the value
        else:
            if self.right is None:  # go right
                self.right = BSTNode(value)  # repeat search
            else:
                self.right.insert(value)  # insert the value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        if target == self.value:
            return True  # cascades back up
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:  # if target is > self.value
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.containt(target)

            # Return the maximum value found in the tree
    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.right:
            self.right.for_each(fn)  # pass fn

        if self.left:  # same for left
            self.left.for_each(fn)

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
