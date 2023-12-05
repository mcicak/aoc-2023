def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

file_path = '/Users/mc/Desktop/advent2023/01/input.txt'
lines = read_file(file_path)

sum = 0
for line in lines:
    firstDigit = -1
    lastDigit = -1
    for char in line:
        if char.isnumeric() and firstDigit == -1:
            firstDigit = int(char)

        if char.isnumeric():
            lastDigit = int(char)

    numAsString = str(firstDigit)+str(lastDigit)
    num = int(numAsString)
    sum = sum + num

print("∑ = " + str(sum))
