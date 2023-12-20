import random
import os
import time

bingo = []
bingos = []


def ran():
    number = random.randint(1, 90)
    return number


def createCard():
    global bingo
    numbers = []
    for i in range(24):
        num = ran()
        while num in numbers:
            num = ran()
        numbers.append(num)

    numbers.sort()

    bingo = [[numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]],
             [numbers[5], numbers[6], numbers[7], numbers[8], numbers[9]],
             [numbers[10], numbers[11], "BINGO", numbers[12], numbers[13]],
             [numbers[14], numbers[15], numbers[16], numbers[17], numbers[18]],
             [numbers[19], numbers[20], numbers[21], numbers[22], numbers[23]]]


createCard()

cards = int(input("How many cards do you want to play with? "))

for i in range(cards):
    createCard()
    bingos.append(bingo)


def prettyPrintMultiple():
    for bingo in bingos:
        print("Bingo Card id: ", bingos.index(bingo) + 1)
        for row in bingo:
            for item in row:
                print(f"|\t{item}\t", end="|")
            print()
        print()


cache = []

while True:
    prettyPrintMultiple()
    num = random.randint(1, 90)

    while num in cache:
        num = random.randint(1, 90)

    cache.append(num)
    cache.sort()

    print("Next Number: ", num)
    print("Numbers called: ", len(cache))

    # time.sleep(2) # Uncomment this line to slow down the game
    for bingo in bingos:
        for row in range(5):
            for item in range(5):
                if bingo[row][item] == num:
                    bingo[row][item] = "X"

    exes = []

    for bingo in bingos:
        exes.append(0)
        for row in bingo:
            for item in row:
                if item == "X":
                    exes[bingos.index(bingo)] += 1
        print("Exes in card id: ", bingos.index(bingo) +
              1, " is: ", exes[bingos.index(bingo)])

        if exes[bingos.index(bingo)] == 24:
            print("\n\nBINGO!!!")
            print("Bingo with Card id: ", bingos.index(bingo) + 1, "has won!")
            for row in bingo:
                for item in row:
                    print(item, end="\t|\t")
                print()
            print()
            exit()

    time.sleep(1)
    os.system("clear")
