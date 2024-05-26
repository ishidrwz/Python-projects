# display user choice
def display():
    print("R:Rock,S:Scissor,P:Paper")


# check who is winner
def checkwin(user1, user2):
    if user1 == user2:
        return 0
    elif (
        user1 == "R"
        and user2 == "S"
        or user1 == "S"
        and user2 == "P"
        or user1 == "P"
        and user2 == "R"
    ):
        return 1
    else:
        return 2


score = {"PLAYER1": 0,"PLAYER2": 0,}

# count score
def scorecard(score, p1=0, p2=0):
    if p1 == 1:
        score["PLAYER1"] += 1
    elif p2 == 1:
        score["PLAYER2"] += 1
    return score


import random


def main():
    l = ["S", "P", "R"]
    ch = {"R": "Rock", "P": "Paper", "S": "Scissor"}
    display()

    while True:
        while True:
            user1 = input("Enter your choice: ")
            if user1 not in ch:
                print("invalid input")
            else:
                break
        user2 = random.choice(l)
        print()
        print("----------------------------------------------------")
        print("  ", "|", "Player1 chose:", ch[user1], "Computer chose:", ch[user2], "|")
        print("----------------------------------------------------")

        if checkwin(user1, user2) == 1:
            p1 = 1
            print("🎉PLAYER1 WINS!! THE ROUND🎉")
            scorecard(score, p1, p2=0)
            break
        elif checkwin(user1, user2) == 2:
            p2 = 1
            print("🎉COMPUTER WINS!! THE ROUND🎉")
            scorecard(score, p2=p2)
            break
        else:
            print("TIE!🤝")
        print()


main()
while True:
    print('       🟢CURRENT SCORE🟢','\n',scorecard(score))
    print()
    cont = input("ANOTHER GAME?,Y/N")
    print()
    if cont.lower() == "y":
        main()
    else:
        print("-----------------------------")
        print('       🏆FINAL SCORE🏆','\n',scorecard(score))
        print("-----------------------------")
        print()
        if score["PLAYER1"] > score["PLAYER2"]:
            print("🏅 PLAYER1 WINS!! 🏅")
        elif score["PLAYER1"] < score["PLAYER2"]:
            print("🏅 PLAYER2 WINS!! 🏅")
        else:
            print("TIE!!🏳️")
        break
