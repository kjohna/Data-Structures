"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    # wap the new value in a ListNode
    new_head = ListNode(value)
    # if the ll is empty:
    if self.length == 0:
        self.head = new_head
        self.tail = new_head
        self.length += 1
        return value
    # order important here:
    # set curr head's previous to point to new_head
    self.head.previous = new_head
    # set new_head's next to point to curr head
    new_head.next = self.head
    # finally reassign self.head
    self.head = new_head    
    self.length += 1
    return value

  def remove_from_head(self):
    # get the value before removing
    value = self.head.value
    # reassign head to curr head's next 
    self.head = self.head.next
    # if the head wasn't the only value
    if self.head.prev:
        # prev points to None
        self.head.prev = None
    self.length -= 1
    return value

  def add_to_tail(self, value):
    # wrap the new value in a ListNode
    new_tail = ListNode(value)
    # if the ll is empty:
    if self.length == 0:
        self.head = new_tail
        self.tail = new_tail
        self.length += 1
        return value
    # curr tail's next now points to new_tail
    self.tail.next = new_tail
    # new_tail's prev points to curr tail
    new_tail.prev = self.tail
    # finally, reassign self.tail
    self.tail = new_tail
    self.length += 1
    return value

  def remove_from_tail(self):
    # get the value before removing
    value = self.tail.value
    # reassign tail to curr tail's prev
    self.tail = self.tail.prev
    # if the tail wasn't the only value
    if self.tail.next:
        # tail's next points to None
        self.tail.next = None
    self.length -= 1
    return value

  def move_to_front(self, node):
    # if node is head:
    if node == self.head:
        return node.value
    # extract the node
    # 1. node's prev must point to node's next
    node.prev.next = node.next
    # if node is the tail, node's prev is now the tail:
    if node.next == None:
        self.tail = node.prev
    # otherwise, node's next must point to node's prev
    else:
        node.next.prev = node.prev
    # replace head
    # curr head's prev points to node
    self.head.prev = node
    # node's next points to curr head
    node.next = self.head
    # node's prev points to None
    node.prev = None
    # reassign head
    self.head = node
    return node.value

  def move_to_end(self, node):
    # if node is tail
    if node == self.tail:
        return node.value
    # extract the node
    # 1. node's prev must point to node's next
    # if node is the head, node's next is now the head:
    if node.prev == None:
        self.head = node.next
    # otherwise, node's prev must point to node's next
    else:
        node.prev.next = node.next
    # 2. node's next must point to node's prev
    node.next.prev = node.prev
    # replace the tail
    # curr tail's next points to node
    self.tail.next = node
    # node's prev points to curr tail
    node.prev = self.tail
    # node's next points to None
    node.next = None
    # reassign tail
    self.tail = node
    return node.value

  def delete(self, node):
    # if node is only node
    if node == self.head and node == self.tail:
        self.head = None
        self.tail = None
    # if node is current head
    elif node == self.head:
        node.next.prev = None
        self.head = node.next
    # if node is current tail
    elif node == self.tail:
        node.prev.next = None
        self.tail = node.prev
    # if node is in the middle
    else:
        node.prev.next = node.next
        node.next.prev = node.prev
    # update length
    self.length -= 1
    
  def get_max(self):
    curr_node = self.head
    curr_max = float("-inf")
    while curr_node:
        if curr_node.value > curr_max:
            curr_max = curr_node.value
        curr_node = curr_node.next
    return curr_max
