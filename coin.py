from random import choice

def showIt():
    showIt = input("want to see result of each flip? (y/n)").lower()
    if showIt not in ["y","n"]:
        print("Use \'y\' or \'n\'")
        showIt()
    return showIt

def main():
    times = int(input("How many times you want to flip a coin? : "))
    possibleOutputs = ['HEADS','TAILS']
    tails = 0
    heads = 0
    showresults = showIt()

    for x in range(times):
        side = choice(possibleOutputs)
        if side == "TAILS":
            tails += 1
        else:
            heads += 1
        if showresults.startswith('y'): print(side)
        if tails == heads: print(f"At {x} flips, the number of heads and tail were equal at {heads} each")
    print(f"TAILS = {tails}/{times} | % -> {(tails/times) * 100}%")
    print(f"HEADS = {heads}/{times} | % -> {(heads/times) * 100}%")

if __name__ == "__main__":
    main()

    