class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node
    
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    # add element to the list's tail
    def add_element(self, value):
        new_element = Node(value)
        # if the list is empty
        if not self.head and not self.tail:
            self.head = new_element
            self.tail = new_element
        # if the list is not empty
        else:
            # order here is important!
            self.tail.set_next(new_element)
            self.tail = new_element
        return True

    # remove element from head
    def remove_head(self):
        # if list is empty
        if not self.head and not self.tail:
            return None
        # if list is only one node
        if self.head == self.tail:
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head.get_value()
        # if list has more than one node
        else:
            old_head = self.head
            self.head = self.head.get_next()
            return old_head.get_value()

    def find_element(self, value):
        # if list is empty:
        if not self.head and not self.tail:
            return None
        # start with head, move to tail
        check = self.head
        while check:
            # found the value
            if check.get_value() == value:
                return True
            check = check.get_next()
        # didn't find the value
        return False



