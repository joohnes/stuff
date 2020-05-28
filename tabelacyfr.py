
def tit(func, *args):
    from timeit import default_timer
    starttime = default_timer()
    func(args[0])
    print(f"starttime is: {starttime}")
    return default_timer() - starttime

def tabela(liczba: int):
    """Returns number of digits in a number and sorted digits \n
    return (length, list)
    """
    return (len(str(liczba)), sorted(int(x) for x in list(str(liczba))))
if __name__ == '__main__':
    print(tabela(242))
    print(tit(tabela,242))