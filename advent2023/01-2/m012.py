def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return map(lambda x: x.strip(), lines)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


def calculateSum(lines):
    sum = 0
    for line in lines:
        firstDigit = -1
        lastDigit = -1
        for char in line:
            if char.isnumeric() and firstDigit == -1:
                firstDigit = int(char)

            if char.isnumeric():
                lastDigit = int(char)

        numAsString = str(firstDigit) + str(lastDigit)
        num = int(numAsString)
        sum = sum + num
    return sum


def convertTxt2Int(lines):
    txt2int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    def convert(input):
        ret = str(input)
        keys = txt2int.keys()

        builder = ""
        hasNextLetter = True
        i = 0
        while hasNextLetter:
            substring = input[i:]

            digitAppended = False
            for key in keys:
                if substring.startswith(key):
                    builder += str(txt2int[key])
                    ret = ret.replace(key, str(txt2int[key]))

            if not digitAppended:
                builder += input[i]

            i += 1
            hasNextLetter = len(input) -1 >= i

        return builder

    return list(map(convert, lines))

file_path = '/01-2/input.txt'

lines = read_file(file_path)

lines = convertTxt2Int(lines)
sum = calculateSum(lines)

print("∑ = " + str(sum))
