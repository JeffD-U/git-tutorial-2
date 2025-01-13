"""
CMSC 14200, Winter 2025
Homework #1, Task #2

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from tree import TreeNode

def increasing_paths(t: TreeNode) -> list[list[int]]:
   """
   Given a tree, produce a list of all root-to-leaf paths where the values
   in the path are in increasing order.

   Args:
      t: Tree

   Returns: List of all root-to-leaf paths (where each path is a list
      of root-to-leaf values) where the values in the path are in increasing
      order
   """
   #basecase
   list1 = []
   if t.is_leaf():
      return [[t.value]]
   #recursivecase
   else:
      for child in t.children:
         if child.value > t.value:
            for path in increasing_paths(child):
               list1.append([t.value] + path)
   return list1

