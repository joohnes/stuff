def armstrong(number: int):
    final = 0
    for x in str(number):
        final += pow(int(x), len(str(number)))
    return final == number


print(f"{armstrong(6)}")
print(f"{armstrong(407)}")
print(f"{armstrong(2278)}")


