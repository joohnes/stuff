
def tit(func, *args):
    from timeit import default_timer
    starttime = default_timer()
    func(args[0])
    return default_timer() - starttime

def tabela(liczba: int):
    """Zwraca liczbę cyfr i posortowaną tabelę"""
    return (len(str(liczba)), sorted(int(x) for x in list(str(liczba))))

print(tabela(242))
print(tit(tabela,242))