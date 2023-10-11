#!/usr/bin/python3
"""contains Pascal_triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the triangle"""

    if n <= 0:
        return []

    list_triangles = [[1]]
    while len(list_triangles) != n:
        triangles = list_triangles[-1]
        temp = [1]

        for i in range(len(triangles) - 1):
            temp.append(triangles[i] + triangles[i + 1])
        temp.append(1)
        list_triangles.append(temp)

    return list_triangles
