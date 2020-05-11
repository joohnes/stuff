from os import listdir, mkdir
from shutil import copyfile
PATH = input("COPY PATH: ")
PathToFile = input("Path to name file: ")
howMany = int(input("How many photos do you want to assign to one title? "))
specifier = input("What are specifiers? (separated by space)")
specifiers = specifier.split()

with open(PathToFile,"r") as f:
    data = f.readlines()
data = [x.strip() for x in data]
data = [x.split() for x in data]
processed = []
for x in data:
    part = []
    for i in x:
        if i == '-':
            break
        part.append(i)
    processed.append(part)

try:
    mkdir(PATH+'/copied')
except FileExistsError:
    print("Directory \'copied\' already exists")

files = sorted(listdir(PATH))
extension = files[1].split(".")[1]
def createNames():
    counter = 0
    while True:
        yield f"{specifiers[counter]}"
        counter += 1

counter = 0
for x in processed:
    name = "_".join(x)
    spec = createNames()
    extension = files[counter].split('.')[1]
    for i in range(howMany):
        copyfile(PATH + "/" + files[counter],f"{PATH}/copied/{name}_{next(spec)}.{extension}")
        counter += 1
