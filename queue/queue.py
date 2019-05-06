from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    added = self.storage.add_element(item)
    if added:
        self.size += 1
        return True
    return False
  
  def dequeue(self):
    dequeued = self.storage.remove_head()
    if dequeued:
        self.size -= 1
    return dequeued

  def len(self):
    return self.size
