# from __future__ import annotations
from functools import reduce


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return map(lambda x: x.strip(), lines)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


# lines = list(read_file("/Users/mc/Desktop/aoc-2023/advent2023/10/input-small.txt"))


lines = list(read_file("/Users/mc/Desktop/aoc-2023/advent2023/10/input.txt"))

class Node:

    def __init__(self, parent: 'Node' = None):
        self.parent = parent
        self.children = []


def lines_to_matrix(lines):
    # Assuming all lines have the same length
    width = len(lines[0])

    # Create a 2D matrix filled with zeros
    matrix = [[' ' for _ in range(width)] for _ in range(len(lines))]

    # Fill the matrix with characters from the lines
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            matrix[i][j] = char

    return matrix


def nextNode(world, path):
    last = path[-1]
    x = last[0]
    y = last[1]
    lastChar = world[y][x]

    ret = (0, 0)
    if lastChar == "|":
        candidates = [(x, y - 1), (x, y + 1)]
        if candidates[0] in path:
            candidates.remove(candidates[0])
        elif candidates[1] in path:
            candidates.remove(candidates[1])

        ret = candidates[0]

    if lastChar == "-":
        candidates = [(x - 1, y), (x + 1, y)]
        if candidates[0] in path:
            candidates.remove(candidates[0])
        elif candidates[1] in path:
            candidates.remove(candidates[1])

        ret = candidates[0]

    if lastChar == "L":
        candidates = [(x, y - 1), (x + 1, y)]
        if candidates[0] in path:
            candidates.remove(candidates[0])
        elif candidates[1] in path:
            candidates.remove(candidates[1])

        ret = candidates[0]

    if lastChar == "J":
        candidates = [(x - 1, y), (x, y - 1)]
        if candidates[0] in path:
            candidates.remove(candidates[0])
        elif candidates[1] in path:
            candidates.remove(candidates[1])

        ret = candidates[0]

    if lastChar == "7":
        candidates = [(x - 1, y), (x, y + 1)]
        if candidates[0] in path:
            candidates.remove(candidates[0])
        elif candidates[1] in path:
            candidates.remove(candidates[1])

        ret = candidates[0]

    if lastChar == "F":
        candidates = [(x, y + 1), (x + 1, y)]
        if candidates[0] in path:
            candidates.remove(candidates[0])
        elif candidates[1] in path:
            candidates.remove(candidates[1])

        ret = candidates[0]

    return ret


S = (0, 0)
world = lines_to_matrix(lines)

for i in range(len(lines)):
    line = lines[i]
    if "S" in line:
        y = i
        x = list(line).index("S")
        S = (x, y)
        break

path1 = [S, (31, 27)]
path2 = [S, (31, 25)]
path1C = ["S", "J"]
path2C = ["S", "|"]

end = False

i = 1
while not end:
    path1.append(nextNode(world, path1))
    path2.append(nextNode(world, path2))

    p1 = path1[-1]
    p2 = path2[-1]
    c1 = world[p1[1]][p1[0]]
    c2 = world[p2[1]][p2[0]]
    path1C.append(c1)
    path2C.append(c2)

    i += 1
    if path1[-1] == path2[-1]:
        end = True

print(i)
