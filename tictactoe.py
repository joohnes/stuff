from termcolor import cprint, colored

gameboard = {
"1": "_",
"2": "_",
"3": "_",
"4": "_",
"5": "_",
"6": "_",
"7": "_",
"8": "_",
"9": "_",
}
CURRENTPLAYER = True

def showGameboard():
    print( "        Tic-Tac-Toe")
    print( "     ~~~~~~~~~~~~~~~~~     info: ~~~~~~~~~~~~~~~~~")
    print(f"     || {list(gameboard.values())[0]} || {list(gameboard.values())[1]} || {list(gameboard.values())[2]} ||           || {list(gameboard.keys())[0]} || {list(gameboard.keys())[1]} || {list(gameboard.keys())[2]} ||")
    print( "     ~~~~~~~~~~~~~~~~~     info: ~~~~~~~~~~~~~~~~~")
    print(f"     || {list(gameboard.values())[3]} || {list(gameboard.values())[4]} || {list(gameboard.values())[5]} ||           || {list(gameboard.keys())[3]} || {list(gameboard.keys())[4]} || {list(gameboard.keys())[5]} ||")
    print( "     ~~~~~~~~~~~~~~~~~     info: ~~~~~~~~~~~~~~~~~")
    print(f"     || {list(gameboard.values())[6]} || {list(gameboard.values())[7]} || {list(gameboard.values())[8]} ||           || {list(gameboard.keys())[6]} || {list(gameboard.keys())[7]} || {list(gameboard.keys())[8]} ||")
    print( "     ~~~~~~~~~~~~~~~~~     info: ~~~~~~~~~~~~~~~~~\n")

def getInput():
    global CURRENTPLAYER
    while True:
        if CURRENTPLAYER:
            move = input("X: Where would you like to place your piece? (1-9): ")
        else:
            move = input("O: Where would you like to place your piece? (1-9): ")

        try:
            move = int(move)
        except Exception as e:
            print(f"Please use only numbers from 1-9!")
            continue

        if move < 1 or move > 9:
            print("Please choose number from 1 to 9")
            continue
        break

    if CURRENTPLAYER:
        gameboard[str(move)] = colored("X", "cyan")
    else:
        gameboard[str(move)] = colored("O", "yellow")

    CURRENTPLAYER = not CURRENTPLAYER

def hasWon():
    if gameboard["1"] == gameboard["2"] == gameboard["3"] != "_":
        showGameboard()
        cprint(f"{gameboard['1'][5:-4]} has won the game!", "green") # 1 -
        return False

    if gameboard["4"] == gameboard["5"] == gameboard["6"] != "_":
        showGameboard()
        cprint(f"{gameboard['4'][5:-4]} has won the game!", "green") # 2 -
        return False

    if gameboard["7"] == gameboard["8"] == gameboard["9"] != "_":
        showGameboard()
        cprint(f"{gameboard['7'][5:-4]} has won the game!","green") # 3 -
        return False

    if gameboard["1"] == gameboard["4"] == gameboard["7"] != "_":
        showGameboard()
        cprint(f"{gameboard['1'][5:-4]} has won the game!","green") # 1 |
        return False

    if gameboard["2"] == gameboard["5"] == gameboard["8"] != "_":
        showGameboard()
        cprint(f"{gameboard['2'][5:-4]} has won the game!","green") # 2 |
        return False

    if gameboard["3"] == gameboard["6"] == gameboard["9"] != "_":
        showGameboard()
        cprint(f"{gameboard['3'][5:-4]} has won the game!","green") # 3 |
        return False

    if gameboard["3"] == gameboard["5"] == gameboard["7"] != "_":
        showGameboard()
        cprint(f"{gameboard['3'][5:-4]} has won the game!","green") # /
        return False

    if gameboard["1"] == gameboard["5"] == gameboard["9"] != "_":
        showGameboard()
        cprint(f"{gameboard['1'][5:-4]} has won the game!","green") # \
        return False
    return True

def main():
    while hasWon():
        showGameboard()
        getInput()

if __name__ == "__main__":
    main()
