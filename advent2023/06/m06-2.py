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
    return [int(s.strip()) for s in string.split() if s.strip()]

#lines = read_file("/Users/mc/Desktop/advent2023/06/input-small.txt")
lines = read_file("/Users/mc/Desktop/advent2023/06/input.txt")
lines = [string for string in lines if string != ""]

time = int(lines[0].split(":")[1].replace(" ",""))
distance = int(lines[1].split(":")[1].replace(" ",""))

failures = 0
for i in range(time):
    print(f"{i/time*100} %")
    v = i
    t = time - i
    s = t * v
    if s <= distance:
        failures += 1

success = time - failures
print(success)
