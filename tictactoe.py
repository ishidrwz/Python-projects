# display grid function
def display(grid): 
    for i in range(0, len(grid), 3):
        print(' | '.join(grid[i:i + 3]))
        if i < 6:
            print('---------')


score = {"player1": 0, "player2": 0}


def scorecard(score, p1, p2):
    if p1 == 1:
        score["player1"] += 1
    elif p2 == 1:
        score["player2"] += 1
    return score



# main function
def tictactoe():
    grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numch = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    display(grid)
    p1 = 0
    p2 = 0

    while len(numch) != 0:
        check = len(numch)
        if check != 0:
            # player1 turn
            while True:
                user1 = int(input("PLAYER1 TURN , enter number b/w 1-9: "))
                if user1 in numch:
                    grid[user1 - 1] = "o"
                    numch.discard(user1)
                    break
                else:
                    # display the move
                    display(grid)
                    print("invalid input,enter again")

            # display the move
            display(grid)

            # check if player1 wins
            if (
                grid[0] == "o"
                and grid[1] == "o"
                and grid[2] == "o"
                or grid[3] == "o"
                and grid[4] == "o"
                and grid[5] == "o"
                or grid[6] == "o"
                and grid[7] == "o"
                and grid[8] == "o"
                or grid[0] == "o"
                and grid[3] == "o"
                and grid[6] == "o"
                or grid[1] == "o"
                and grid[4] == "o"
                and grid[7] == "o"
                or grid[2] == "o"
                and grid[5] == "o"
                and grid[8] == "o"
                or grid[0] == "o"
                and grid[4] == "o"
                and grid[8] == "o"
                or grid[2] == "o"
                and grid[4] == "o"
                and grid[6] == "o"
            ):
                print("player1 wins!!")
                p1 += 1
                scorecard(score, p1, p2)
                return
        else:
            break

        check = len(numch)

        if check != 0:
            # player2 turn
            while True:
                user2 = int(input("PLAYER2 TURN , enter number: "))
                if user2 in numch:
                    grid[user2 - 1] = "x"
                    numch.discard(user2)
                    break
                else:
                    # display the move
                    display(grid)
                    print("invalid input,enter again")

            # display the move
            display(grid)

            # check if player2 wins
            if (
                grid[0] == "x"
                and grid[1] == "x"
                and grid[2] == "x"
                or grid[3] == "x"
                and grid[4] == "x"
                and grid[5] == "x"
                or grid[6] == "x"
                and grid[7] == "x"
                and grid[8] == "x"
                or grid[0] == "x"
                and grid[3] == "x"
                and grid[6] == "x"
                or grid[1] == "x"
                and grid[4] == "x"
                and grid[7] == "x"
                or grid[2] == "x"
                and grid[5] == "x"
                and grid[8] == "x"
                or grid[0] == "x"
                and grid[4] == "x"
                and grid[8] == "x"
                or grid[2] == "x"
                and grid[4] == "x"
                and grid[6] == "x"
            ):
                print("player2 wins!!")
                p2 += 1
                scorecard(score, p1, p2)
                return
        else:
            break

    # if no one wins

    print("its a TIE!!")


tictactoe()

while True:
    print(scorecard(score, p1=int, p2=int))
    cont = input("NEW GAME??, enter y/n")
    if cont.lower() == "y":
        tictactoe()
    else:
        if score["player1"] > score["player2"]:
            print("player1 wins")
            break
        elif score["player1"] < score["player2"]:
            print("player2 wins")
            break
        else:
            print("its a tie")
            break
