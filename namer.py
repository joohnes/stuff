from os import rename, listdir, mkdir
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
# counter = 0
for x in processed:
    name = "_".join(x)
    for i in range(howMany):
        # if counter % 2 == 0:
        #     copyfile(PATH + "/" + files[counter],f"{PATH}/copied/{name}_gora.jpeg")
        #     counter += 1
        # else:
        #     copyfile(PATH + "/" + files[counter],f"{PATH}/copied/{name}_dol.jpeg")
        #     counter += 1
