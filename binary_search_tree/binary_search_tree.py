import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

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
    if self.value is None:
      return None
    cb(self.value)
    if self.left is not None:
      self.left.for_each(cb)
    if self.right is not None:
      self.right.for_each(cb)

# DAY 2 Project -----------------------

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_print(self):
      pass

  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  """
  Breadth first search - queue
  check each level one at a time 
  create a queue
  put root in queue
  while queue is not empty
  pop first item in queue
  check left and right add to queue
  shift 
  go to head of queue and continue 
  """
  def bft_print(self, node):
    pass

  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  """
  Depth first search  
  create a stack
  put root in stack
  while stack is not empty
  pop first item in stack
  check root.left and put it in stack
  check root.right and put it in stack
  go to top of stack and continue
  """
  def dft_print(self, node):
    stack = Stack()
    stack.push(node)
    while stack.len() > 0:
      node_to_check = stack.pop()
      if node_to_check.left:
        stack.push(node_to_check.left)
      if node_to_check.right:
        stack.push(node_to_check.right)
      print(node_to_check.value)

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
    pass

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
    pass

if __name__ == '__main__':
  bst = BinarySearchTree(1)
  bst.insert(8)
  bst.insert(5)
  bst.insert(7)
  bst.insert(6)
  bst.insert(3)
  bst.insert(4)
  bst.insert(2)
  bst.dft_print(bst)