from string import ascii_uppercase,ascii_lowercase, punctuation,digits
from random import *



def rdpass(l,u,symb,dg,ln):
    settings = [l,u,symb,dg,ln]
    if ln < 8:
        return "Пароль должен быть не менее 8 символов!"
    letters = ""

    # Проверка настроек
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
    if not(any(settings[:-1])):
        return ("Нет ни одного типа данных")

    # Добавление каждого элемента из настроек
    else:
        pd = []
        if settings[0]:
            pd.append(choice(ascii_lowercase + "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"))
        if settings[1]:
            pd.append(choice(ascii_uppercase + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"))
        if settings[2]:
            pd.append(choice(punctuation))
        if settings[3]:
            pd.append(choice(digits))
    # Добавление оставшихся элементов
        rem_ln = ln - len(pd)
        if rem_ln > 0:
            for i in range(rem_ln):
                pd.append(choice(letters))
        shuffle(pd)
        pd = "".join(pd)
        return pd




# Ввод настроек пароля
print("Введите параметры:")
l = int(input("Наличие нижнего регистра(1 или 0): ").strip())
u = int(input("Наличие верхнего регистра: ").strip())
symb = int(input("Наличие специальных символов: ").strip())
dg = int(input("Наличие цифр: ").strip())
ln = int(input("Длина пароля(минимум 8 символов): ").strip())

pd = rdpass(l,u,symb,dg,ln)
print(pd)


        