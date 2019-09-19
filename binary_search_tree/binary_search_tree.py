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

  # if there is a left, traverse left, print, then if theres a right, traverse right
  def in_order_print(self):
      if self.value is None:
        return None
      if self.left:
        self.left.in_order_print()
      print(self.value)
      if self.right:
        self.right.in_order_print()

  # checks if queue is not empty, dequeues a node, checks if theres a left,
  # if there is it adds it to the queue
  # then checks if theres a right, if there is, add it to the queue,
  # then print the originally dequeued node and repeat
  def bft_print(self, node):
    queue = Queue()
    queue.enqueue(node)
    while queue.len() > 0:
      node_to_check = queue.dequeue()
      if node_to_check.left:
        queue.enqueue(node_to_check.left)
      if node_to_check.right:
        queue.enqueue(node_to_check.right)
      print(node_to_check.value)

  # checks if the stack is not empty, pops the first node off the stack, 
  # checks if there is a left, if there is, pushes node to stack,
  # then checks if there is a right, if there is, pushes it to stack,
  # then prints the first popped node, and repeats
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
  bst = BinarySearchTree(3)
  bst.insert(8)
  bst.insert(5)
  bst.insert(7)
  bst.insert(6)
  bst.insert(10)
  bst.insert(4)
  bst.insert(2)
  bst.in_order_print()