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


class Galaxy:

    def __init__(self, idx, x, y):
        self.idx = idx
        self.x = x
        self.y = y


#lines = list(read_file("/Users/mc/Desktop/aoc-2023/advent2023/11/input-small.txt"))
lines = list(read_file("/Users/mc/Desktop/aoc-2023/advent2023/11/input.txt"))

# expand rows
rowsToInsert = []
columnsToInsert = []

for i in range(len(lines)):
    line = lines[i]
    if not "#" in line:
        rowsToInsert.append(i)

# expand columns
for i in range(len(lines[0])):
    noGalaxy = True
    for j in range(len(lines)):
        line = lines[j]
        if line[i] == "#":
            noGalaxy = False

    if noGalaxy:
        columnsToInsert.append(i)

dots = '.' * len(lines[0])
for i in reversed(rowsToInsert):
    lines.insert(i, dots)

for i in reversed(columnsToInsert):
    for j in range(len(lines)):
        line = lines[j]
        newLine = line[:i] + "." + line[i:]
        lines[j] = newLine

galaxies = []
distances = []
idx = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        char = lines[i][j]
        if char == "#":
            galaxies.append(Galaxy(idx, i, j))
            idx += 1

print("G COUNT: " + str(len(galaxies)))

for i in range(len(galaxies) - 1):
    galaxy1 = galaxies[i]
    for j in range(galaxy1.idx + 1, len(galaxies)):
        galaxy2 = galaxies[j]
        s = abs(galaxy2.x - galaxy1.x) + abs(galaxy2.y - galaxy1.y)
        distances.append(s)

sum = reduce(lambda x, y: x + y, distances)
print(sum)
