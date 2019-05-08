class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        # default is max heap
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        iv = len(self.storage) - 1
        # bubble up
        self._bubble_up(iv)

    def delete(self):
        # if only one element, pop and return
        if len(self.storage) == 1:
            return self.storage.pop()
        # store first value
        first = self.storage[0]
        # replace first element with last & remove last element
        self.storage[0] = self.storage.pop()
        self._sift_down(0)
        return first

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # if value is the first element, done
        if index == 0:
            return
        value = self.storage[index]
        ip = (index - 1) // 2
        parent = self.storage[ip]
        while self.comparator(value, parent):
            # swap if value satisfies comparator relative to parent
            self.storage[index], self.storage[ip] = parent, value
            # update index
            index = ip
            if index == 0:
                # done
                return
            # set ip to new parent, update parent value
            ip = (index - 1) // 2
            parent = self.storage[ip]

    def _sift_down(self, index):
        parent = self.storage[index]
        il = 2 * index + 1
        # if left child doesn't exist we're done
        if len(self.storage) == il:
            return
        cl = self.storage[il]
        ir = 2 * index + 2
        # if right child doesn't exist, swap parent with left child if left child doesn't fit comparator
        if len(self.storage) == ir:
            if self.comparator(cl, parent):
                self.storage[il], self.storage[index] = parent, cl
                return
        cr = self.storage[ir]
        # if either of parent's children satisfy the comparator, sift down
        while self.comparator(cl, parent) or self.comparator(cr, parent):
            # priority to child which is more satisfactory
            if self.comparator(cl, cr):
                self.storage[il], self.storage[index] = parent, cl
                index = il
            else:
                self.storage[ir], self.storage[index] = parent, cr
                index = ir
            # update parent, left & right children
            il = 2 * index + 1
            # if left child doesn't exist we're done
            if len(self.storage) < il + 1:
                return
            cl = self.storage[il]
            ir = 2 * index + 2
            # if right child doesn't exist, swap parent with left child if parent is smaller, done
            if len(self.storage) < ir + 1:
                if self.comparator(cl, parent):
                    self.storage[il], self.storage[index] = parent, cl
                return
            cr = self.storage[ir]

