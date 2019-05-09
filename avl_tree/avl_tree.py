"""
Node class to keep track of
the data internal to individual nodes
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Return True if node has no subtrees
    """

    def is_leaf(self):
        # if no node, true
        if not self.node:
            return True
        # if node has no children, true
        if not self.node.left and not self.node.right:
            return True
        return False

    """
    Display the whole tree. Uses recursive def.
    """

    def display(self, level=0, pref=""):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None:
            print(
                "-" * level * 2,
                pref,
                self.node.key,
                "[h" + str(self.height) + ":b" + str(self.balance) + "]",
                "L" if self.is_leaf() else " ",
            )
            if self.node.left != None:
                self.node.left.display(level + 1, "<")
            if self.node.right != None:
                self.node.right.display(level + 1, ">")

    """
    Computes the maximum number of levels there are
    in the tree
    """

    def update_height(self):
        # recursive helper to determine height of node
        def node_height(node):
            if node:
                return node.update_height()
            else:
                return -1

        # check right and left
        rh = 1 + node_height(self.node.right)
        lh = 1 + node_height(self.node.left)
        self.height = max(rh, lh)
        return self.height

    """
    Updates the balance factor on the AVLTree class
    """

    def update_balance(self):
        # check (if) left and right children, compute balance factor
        rh = 0
        if self.node.right:
            rh = self.node.right.height
            self.node.right.update_balance()
        lh = 0
        if self.node.left:
            lh = self.node.left.height
            self.node.left.update_balance()
        self.balance = rh - lh

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """

    def _left_rotate(self):
        pass

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """

    def _right_rotate(self):
        pass

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """

    def rebalance(self):
        pass

    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """

    def insert(self, key):
        # if AVLTree is initialized without node:
        if not self.node:
            self.node = Node(key)
            self.update_height()
            return
        # if key we're trying to insert is less, go left
        if key < self.node.key:
            # if a left leaf exists, insert there
            if self.node.left:
                self.node.left.insert(key)
            # else, create left leaf with key
            else:
                self.node.left = AVLTree(Node(key))
                self.update_height()
        # else, go right
        else:
            # if a right leaf exists, insert there
            if self.node.right:
                self.node.right.insert(key)
            # else, create right leaf with key
            else:
                self.node.right = AVLTree(Node(key))
                self.update_height()
        print("\n AVL Tree: \n")
        self.display()
        print("\n")

