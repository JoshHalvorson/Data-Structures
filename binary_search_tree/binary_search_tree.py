#import sys
#sys.path.append('../queue_and_stack')
#from dll_queue import Queue
#from dll_stack import Stack

# Questions:
# Only ints? 
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
  def __init__(self, value): # We're just using value, so key is value
    self.value = value
    self.left = None
    self.right = None

  # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert
  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  # * `contains` searches the binary search tree for the input value, 
  # returning a boolean indicating whether the value exists in the tree or not.
  # Start from root and traverse the tree
  # We can stop at the first instance of a value
  # We know it's not found if we get to a node that doesn't have children
  def contains(self, target):
    if self.left and target < self.value:
      return self.left.contains(target)
    elif self.right and target >= self.value:
      return self.right.contains(target)
    elif target is self.value:
      return True
    else:
      return False

  # * `get_max` returns the maximum value in the binary search tree.
  def get_max(self):
    root = self.value
    left_max = 0
    right_max = 0
    
    if self.value is None:
      return None
    if self.left is not None:
      left_max = self.left.get_max()
    if self.right is not None:
      right_max = self.right.get_max()

    if left_max > root:
      root = left_max
    if right_max > root:
      root = right_max
    return root


  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):
    pass
