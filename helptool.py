import os

DECISIONS = ['delete','move','copy']

def deleteFiles(path, selected, specifier):
    for i in selected:
        os.remove(f"{PATH}/{i}")

def getDecision():
    message = '(q to quit) '
    for x in DECISIONS:
        message += x.upper() + ' | '
    decision = input(message[:-2]).lower()
    if (decision not in DECISIONS) and decision != 'q':
        print("This is not a valid option.")
        getDecision()
    if decision == 'q':
        exit(0)
    return decision

def main():
    decision = getDecision()
    PATH = input("COPY FULL PATH: ")
    dir = os.listdir(PATH)
    specifier = input("ENTER SPECIFIER: ")
    selectedFiles = []
    for x in dir:
        if char in x:
            selectedFiles.append(x)
    if decision == 'delete':
        deleteFiles(PATH, selectedFiles, specifier)
    elif decision == 'move':
        pass
    elif decision == 'copy':
        pass

if __name__ == '__main__':
    main()
