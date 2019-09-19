import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?

    # quicker to move elements around in our queue
    self.storage = DoublyLinkedList()

  def enqueue(self, value):
    self.storage.add_to_head(value)
    self.size += 1
      
  def dequeue(self):
    if self.len() > 0:
      val = self.storage.tail.value
      self.storage.remove_from_tail()
      self.size -= 1
      return val
    return None

  def len(self):
    return self.size
  
