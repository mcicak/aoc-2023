from functools import reduce


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


# lines = list(read_file("/Users/mc/Desktop/aoc-2023/advent2023/08/input-small1.txt"))
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

steps = 0

node = nodesMap["AAA"]
while node.key != "ZZZ":
    nextStep = walkPattern[steps % len(walkPattern)]
    node = nodesMap[node.left] if nextStep == "L" else nodesMap[node.right]
    steps += 1


print(steps)
