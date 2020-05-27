def IsOldEnough():
    age = int(input("What is your age?: "))
    if age > 17:
        return True
    else:
        return False


def main():
    parties = {
        "Republican": 'a major',
        "Democratic": 'not a major',
        "Independent": 'not a major',
        "Libertarian": 'not a major',
        "Green": 'not a major'
    }
    name = input("Enter your name: ")
    if IsOldEnough():
        print(
            f"Congratulations {name.capitalize()}! You are old enough to vote!")
        print("Here is a list of political parties to join:")
        for x in parties:
            print(f"    - {x}")
        print("\n")
        choice = input(
            "What party would you like to join? : ").lower().capitalize()
        if choice in parties:
            print(f"You have joined the {choice} party!")
            print(f"This is {parties[choice]} party.")
        else:
            print("there is no such party.")
    else:
        print("You are too young to vote.")


if __name__ == "__main__":
    main()
