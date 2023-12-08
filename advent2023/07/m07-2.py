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


cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
cards1 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def bestHand(handList):
    if "J" not in handList:
        return handList

    handString = ''.join(handList)
    maxType = Hand(handString.replace("J", "A"), 1).type()
    maxHandString = handString.replace("J", "A")
    for card in cards1:
        newHandString = handString.replace("J", card)
        hand = Hand(newHandString, 1)
        if hand.type() > maxType:
            maxType = hand.type()
            maxHandString = newHandString

    return maxHandString


class Hand:

    def __init__(self, handString, bid):
        self.hand = list(handString)
        self.bid = bid
        self.best = handString
        if "J" in self.hand:
            self.best = bestHand(handString)

        self.cardTypeCounts = {}

        for card in self.best:
            self.cardTypeCounts[card] = self.cardTypeCounts.get(card, 0) + 1

        self.sortedCardTypeCounts = list(reversed(sorted(list(self.cardTypeCounts.values()))))

    def type(self):
        if len(self.sortedCardTypeCounts) == 1:
            return 7

        if self.sortedCardTypeCounts[0] == 4:
            return 6

        if len(self.sortedCardTypeCounts) == 2 and self.sortedCardTypeCounts[0] == 3:
            return 5

        if len(self.sortedCardTypeCounts) == 3 and self.sortedCardTypeCounts[0] == 3:
            return 4

        if len(self.sortedCardTypeCounts) == 3 and self.sortedCardTypeCounts[0] == 2:
            return 3

        if len(self.sortedCardTypeCounts) == 4:
            return 2

        return 1

    def __lt__(self, other):
        if self.type() != other.type():
            return self.type() > other.type()

        for i in range(5):
            myCard = self.hand[i]
            otherCard = other.hand[i]
            myIndex = cards.index(myCard)
            otherIndex = cards.index(otherCard)
            if myIndex != otherIndex:
                return myIndex < otherIndex

        return False

    def __eq__(self, other):
        return self.hand == other.hand and self.bid == other.bid

# lines = read_file("/Users/mc/Desktop/aoc-2023/advent2023/07/input-small.txt")
lines = read_file("/Users/mc/Desktop/aoc-2023/advent2023/07/input.txt")
hands = list(map(lambda x: Hand(x.split()[0], int(x.split()[1])), lines))
s1 = sorted(hands)
sortedHands = list(reversed(s1))

sum = 0
for i in range(len(sortedHands)):
    hand = sortedHands[i]
    sum += hand.bid * (i+1)

print(sum)
