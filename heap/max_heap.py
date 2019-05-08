class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # append value to storage
        self.storage.append(value)
        iv = len(self.storage) - 1
        # bubble up
        self._bubble_up(iv)

    def delete(self):
        # if only one element, pop and return
        if len(self.storage) == 1:
            return self.storage.pop()
        # store first element
        first = self.storage[0]
        # replace with last element (&remove last element)
        self.storage[0] = self.storage.pop()
        self._sift_down(0)
        return first

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # if value is the first element, done
        if index == 0:
            return
        value = self.storage[index]
        # check index's parent, swap if larger
        # repeat until value's parent is smaller
        pi = (index - 1) // 2
        parent = self.storage[pi]
        while parent < value:
            # swap
            self.storage[pi], self.storage[index] = value, parent
            # update index
            index = pi
            if index == 0:
                # done
                return
            # set pi to new parent, update parent value
            pi = (index - 1) // 2
            parent = self.storage[pi]

    def _sift_down(self, index):
        # sift down new first element until it is where it belongs
        parent = self.storage[index]
        il = 2 * index + 1
        # if left child doesn't exist we're done
        if len(self.storage) == il:
            return
        cl = self.storage[il]
        ir = 2 * index + 2
        # if right child doesn't exist, swap parent with left child if parent is smaller, done
        if len(self.storage) == ir:
            if parent < cl:
                self.storage[il], self.storage[index] = parent, cl
            return
        cr = self.storage[ir]
        while parent < max(cl, cr):
            if cl > cr:
                # left child is larger, swap
                self.storage[il], self.storage[index] = parent, cl
                index = il
            else:
                # right child is larger, swap
                self.storage[ir], self.storage[index] = parent, cr
                index = ir
            # update parent, left&right children
            il = 2 * index + 1
            # if left child doesn't exist we're done
            if len(self.storage) < il + 1:
                return
            cl = self.storage[il]
            ir = 2 * index + 2
            # if right child doesn't exist, swap parent with left child if parent is smaller, done
            if len(self.storage) < ir + 1:
                if parent < cl:
                    self.storage[il], self.storage[index] = parent, cl
                return
            cr = self.storage[ir]
