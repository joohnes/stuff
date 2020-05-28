from tabelacyfr import tabela

def potega(a,n):
    """stupid question"""
    return pow(a,n)

def cotojest(number: int):
    tabeleczka = tabela(number)
    finalnum = 0
    for num in tabeleczka[1]:
        finalnum += potega(num,tabeleczka[0])
    return number == finalnum

print(cotojest(407))
print(cotojest(2278))
print(cotojest(6))