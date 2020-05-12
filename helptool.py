from os import remove, listdir
from termcolor import cprint

def deleteFiles(path, selected):
    for i in selected:
        remove(f"{PATH}/{i}")

def main():
    PATH = input("COPY FULL PATH: ")
    dir = listdir(PATH)
    specifier = input("ENTER SPECIFIER: ")

    try:
        selectedFiles = []
        for x in dir:
            if specifier in x:
                selectedFiles.append(x)

        deleteFiles(PATH, selectedFiles)
    except Exception as e:
        cprint("Could not delete those files.", "red")
        exit()
    cprint(f"{len(selectedFiles)} deleted successfully", "green")

if __name__ == '__main__':
    main()
