import random    #imports the built-in random function

#tells what turn(starts at turn 1) it is and the original score of each player(0)
turn = 1
score1 = 0
score2 = 0


def login():    #get users names and checks that they have entered something
    while True:
        login.name1 = input("What is P1's name: ").strip()
        login.name2 = input("What is P2's name: ").strip()

        if login.name1 != "" and login.name2 != "":
            print()
            break
        else:
            print("Please enter names for both")
            print()


def dice_roll():    #calculates the users random dice roll and calculates total
    global turn, score1, score2
    for i in range(10):
        if turn % 2 == 1:
            total = 0

            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)

            print(login.name1, "rolled a", roll1, "and a", roll2)

            total = roll1 + roll2
            score1 = total + score1

            if total % 2 == 1:
                score1 -= 5
            elif total % 2 != 1:
                score1 += 10

            if roll1 == roll2:
                roll3 = random.randint(1, 6)
                print(login.name1, "got a double so they get to roll again")
                print(login.name1, "rolled a", roll3)
                input("Press ENTER to continue")
                score1 = roll3 + score1

            turn += 1

        elif turn % 2 != 1:
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)

            print(login.name2, "rolled a", roll1, "and a", roll2)
            input("Press ENTER to continue")

            total = roll1 + roll2
            score2 = total + score2

            if total % 2 == 1:
                score2 -= 5
            elif total % 2 != 1:
                score2 += 10

            if roll1 == roll2:
                roll3 = random.randint(1, 6)
                print(login.name2, "got a double so they get to roll again")
                print(login.name2, "rolled a", roll3)
                score1 = roll3 + score1

            print()
            turn += 1
    dice_roll.score1 = score1
    dice_roll.score2 = score2


def winner():    #checks to see if there is a winner
    global score1, score2
    if score1 != score2:
        if score1 > score2:
            o = open("save.txt", "a")
            o.write(login.name1 + " : " + str(score1) + "\n")
            o.close()
            print(login.name1, "is the winner\n")
        elif score1 < score2:
            print(login.name2, "is the winner\n")
            o = open("save.txt", "a")
            o.write(login.name2 + " : " + str(score2) + "\n")
            o.close()


def tie():    #checks to see if there is a tie to determine a winner
    global score1, score2
    if score1 == score2:
        froll1 = 0
        froll2 = 0

        froll1 = random.randint(1, 6)
        froll2 = random.randint(1, 6)

        if froll1 == froll2:
            froll1 = random.randint(1, 6)
            froll2 = random.randint(1, 6)
            print(login.name1, "rolled", froll1)
            print(login.name2, "rolled", froll2)

            winner(score1, score2)
        winner(score1, score2)


def result():    #outputs top 5 results from save file
    score_file = "save.txt"
    score = []
    with open(score_file) as f:
        for line in f:
            score.append(line.strip())
    score.sort(key=lambda x: int(x.split(" : ")[-1]), reverse=True)
    print(score[:5])
