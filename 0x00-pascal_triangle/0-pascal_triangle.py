#!/usr/bin/python3

"""
Module 0-pascal_pascal
"""

def pascal_triangle(n):

    """
    returns a list of integers
    representing Pascal's triangle
    """

    if n <= 0:
      return []

    pascal = [[1]]

   for i in range(n - 1):
       tmp = [0] + pascal[-1] + [0]
       row = []
       for j in range(len(pascal[-1]) + 1):
           row.append(temp[j] + temp[j + 1])
       pascal.append(row)

   return pascal
