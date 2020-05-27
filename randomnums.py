from random import randint, choice
from termcolor import cprint, colored
# colors=['red','green','yellow','blue','magenta','cyan','white']
colors = ['grey', 'red']

string = ''
for x in range(10000):
    string += colored(randint(0, 100), choice(colors))
print(string)
