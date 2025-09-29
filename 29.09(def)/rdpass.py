from string import ascii_uppercase,ascii_lowercase, punctuation,digits
from random import *



def rdpass(l,u,symb,dg,ln):
    settings = [l,u,symb,dg]
    letters = ""
    for i in range(len(settings)):
        if settings[i] == 1:
            if i == 0:
                letters +=ascii_lowercase + "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            elif i == 1:
                letters +=ascii_uppercase + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
            elif i == 2:
                letters += punctuation
            elif i == 3:
                letters += digits
    pd = "".join(choice(letters) for i in range(int(ln)))
    return pd

print("Введите параметры:")
l = input("Наличие верхнего регистра(1 или 0): ")
u = input("Наличие нижнего регистра: ")
symb = input("Наличие специальных символов: ")
dg = input("Наличие цифр: ")
ln = input("Длина пароля: ")

pd = rdpass(l,u,symb,dg,ln)
print(pd)


        