from random import randint
T = [randint(0, 10000000000000000) for x in range(1, 18)]

counter = 0


def rek(x, p, k):
    global counter
    counter += 1
    if p < k:
        s = (p+k)//2
        if T[s] >= x:
            return rek(x, p, s)
        else:
            return rek(x, s+1, k)
    else:
        if T[p] == x:
            return p
        else:
            return -1


print(rek(2020, 5, 14))
print(counter)
