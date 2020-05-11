from os import remove, listdir

def deleteFiles(path, selected, specifier):
    for i in selected:
        remove(f"{PATH}/{i}")

def main():
    PATH = input("COPY FULL PATH: ")
    dir = listdir(PATH)
    specifier = input("ENTER SPECIFIER: ")
    selectedFiles = []
    for x in dir:
        if char in x:
            selectedFiles.append(x)
    deleteFiles(PATH, selectedFiles, specifier)

if __name__ == '__main__':
    main()
