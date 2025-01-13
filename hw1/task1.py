"""
CMSC 14200, Winter 2025
Homework #1, Task #1

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

def merge_dictionaries(dicts: list[dict[str, int]]) -> dict[str, int]:
   """
   Merge a list of dictionaries into a single dictionary,
   where each key maps to the sum of the values of that
   key in the provided dictionaries.

   Args:
      dicts: A list of dictionaries to merge.

   Returns: Merged dictionary
   """
   new_dict: dict[str,int] = {}
   for dict in dicts:
      for i in dict.items():
         if i[0] in new_dict.keys():
            new_dict[i[0]] += i[1]
         else:
            new_dict[i[0]] = i[1]
   return new_dict
