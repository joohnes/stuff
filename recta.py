# zbiory
zbior1 = [[7, 6, 11, 33], 3]
zbior2 = [[15, 12, 10, 6, 5, 1], 5]
zbior3 = [[6, 28, 7, 12, 10, 14, 5, 9, 4, 18], 7]
zbior4 = [[4, 34, 16, 8, 6, 22, 14, 12, 2, 7], 2]


def sprawdz(zbior: list):
    najpole = 0
    for wysokosc in zbior[0]:
        for szerokosc in zbior[0]:
            if wysokosc == szerokosc:
                continue
            pole = wysokosc * szerokosc
            if (pole % zbior[1]) != 0:
                if pole > najpole:
                    najpole = pole
    return najpole


print(sprawdz(zbior1))
print(sprawdz(zbior2))
print(sprawdz(zbior3))
print(sprawdz(zbior4))
