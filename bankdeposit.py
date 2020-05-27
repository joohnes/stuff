def currInfo(info):
    return (f"""=====================\nCurrent Account Information\nName: {info['name'].capitalize()}\nSavings: ${info['savings']}\nChecking: ${info['checking']}\n======================""")


def main():
    infos = {}
    infos["name"] = input("Enter your name: ")
    infos["savings"] = int(input("Enter savings balance: "))
    infos["checking"] = int(input("Enter checking balance: "))
    choice = 'y'
    print(currInfo(infos))
    while choice != 'n':
        account = input("what acc would you like to access ->").lower()
        if account in infos:
            action = input("Which action Deposit/Withdrawal ->").lower()
            if action.lower() in ["withdrawal", "deposit"]:
                howmuch = int(input("How much money: "))
                if action.lower() == 'withdrawal':
                    if (infos[account] - howmuch) < 0:
                        print("You don't have enough money!")
                    else:
                        infos[account] -= howmuch
                        print(currInfo(infos))
                else:
                    infos[account] += howmuch
                    print(currInfo(infos))
            else:
                print("There is no such action")
        else:
            print("There is no such account.")
        choice = input(
            "Would you like to make another transaction? (y/n): ").lower()
        if choice not in ['y', 'n']:
            choice = input("Choice must be y or n").lower()


if __name__ == "__main__":
    main()
