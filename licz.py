
def licz(x):
    if x == 1:
        return 1
    else:
        w = licz(x//2)
        if (x % 2) == 1:
            return w + 1
        else:
            return w - 1
        
        
# print(licz(11))
# print(licz(13))
# print(licz(21))
# print(licz(32))

for x in range(101,1000):
    if licz(x) == 0:
        print(x)
        break