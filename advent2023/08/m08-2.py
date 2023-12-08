from functools import reduce
from math import gcd

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return map(lambda x: x.strip(), lines)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


def stringToInts(string):
    return [int(s.strip()) for s in string.components() if s.strip()]


class Node:

    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


# lines = list(read_file("/Users/mc/Desktop/aoc-2023/advent2023/08/input-small2.txt"))
lines = list(read_file("/Users/mc/Desktop/aoc-2023/advent2023/08/input.txt"))

walkPattern = lines[0]
nodes = []

for l in lines:
    if "=" in l:
        components = l.split("=")
        key = components[0].strip()
        rightPart: str = components[1].strip()
        rightPart = rightPart.replace("(", "")
        rightPart = rightPart.replace(")", "")
        comps = rightPart.split(", ")
        left = comps[0]
        right = comps[1]
        node = Node(key, left, right)
        nodes.append(node)

nodesMap = {node.key: node for node in nodes}

stepsCounts = []

stepNodes = list(filter(lambda x: x.key.endswith("A"), nodes))

i = 0
for node in stepNodes:
    steps = 0
    end = False
    nextNode = node
    while not end:
        nextStep = walkPattern[steps % len(walkPattern)]
        nextNode = nodesMap[nextNode.left] if nextStep == "L" else nodesMap[nextNode.right]
        steps += 1
        if nextNode.key.endswith("Z"):
            stepsCounts.append(steps)
            end = True
    i += 1

stepsCount = stepsCounts.pop()
for steps in stepsCounts:
    stepsCount = stepsCount * steps // gcd(stepsCount, steps)

print(stepsCount)
