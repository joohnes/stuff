from random import choice, randint, sample
from string import ascii_letters, digits

emailtemplates = ['jimmy', '']


def password():
    return (''.join(sample(ascii_letters, 10)))


def email():
    return f"{choice(emailtemplates)+''.join(sample(digits,randint(0,4)))}@gmail.com"


with open("emailspw.txt", "w+") as f:
    f.write(''.join([f"{email()} -> {password()}\n" for x in range(10)]))
