class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # check if value is greater or less than value.
        # choose left for less, right for greater
        if value < self.value:
            if self.left:
                # if left has a node, call its insert
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target):
        # test target against self.value
        # go left if target is smaller, right if larger
        # return True if the value is encountered,
        # False if we reach None
        value = self.value
        if value == target:
            return True
        elif target < value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    def get_max(self):
        # go right until self.right is None. return val
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        # execute cb on self.value and left/right children if they exist
        self.value = cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

