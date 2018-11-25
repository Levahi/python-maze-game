import random
Difficulty = int(input("Choose your difficulty, from 1, 2, or 3.\n"))
randvalue = (random.randint(5,10))
Corridors = (Difficulty*randvalue)
def choose(YNorLR,Q):
    global input1
    input1 = "Input error: input is default"
    if YNorLR == "YN":
        input1 = input(Q)
        if input1 == "yes" or "y" or "Yes" or "Y" or "YES":
            input1 = "y"
        elif input1 == "no" or "n" or "No" or "N" or "NO":
            input1 = "n"
    elif YNorLR == "LR":
        input1 = input(Q)
        if input1 == "left" or "l" or "Left" or "L" or "LEFT":
            input1 = "l"
        elif input1 == "right" or "r" or "Right" or "R" or "RIGHT":
            input1 = "r"

def room(n):
    

print("You enter the maze, looking for your dog.")
while Corridors > 0:
    Corridors = Corridors-1
    choose("LR","Which way, left or right?\n")
    print("You enter the next room")
    