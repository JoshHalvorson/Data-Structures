from doubly_linked_list import DoublyLinkedList 
from doubly_linked_list import ListNode

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.limit = limit
    self.current_num_nodes = 0
    self.dll = DoublyLinkedList()
    self.storage = {}

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    # if key is in cache, move that node in dll to head
    # return value of key in cache
    if key in self.storage.keys():
      self.move_node_to_front(key)
      return self.storage[key]
    return None

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    # if key is in cache, update value in cache, move node in dll to head
    if key in self.storage:
      self.storage[key] = value
      self.move_node_to_front(key)
    # else, check if we are at the limit of the cache
    # if we are, remove node from tail of dll since it was updated the longest time ago
    # remove value in cache
    # decrement num of nodes
    else:
      if self.current_num_nodes is self.limit:
        removed = self.dll.remove_from_tail()
        del self.storage[removed]
        self.current_num_nodes -= 1
      # add new key value pair to cache
      # add new node to head
      # increment num nodes
      self.storage[key] = value
      self.dll.add_to_head(key)
      self.current_num_nodes += 1
  
  # this helper function finds the correct node in the dll and moves it to the head
  def move_node_to_front(self, key):
    node = self.dll.head
    while node is not None:
      if node.value is key:
        self.dll.move_to_front(node)
        break
      node = node.next
    