from string import ascii_uppercase



value = input("Введите шифр(CAPSLOCK и 1 язык): ")
shift = int(input("Введите шаг: "))
Russian_alp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
English_alp = ascii_uppercase

def shifr(value,shift):
    symb = value[0]

    if symb in Russian_alp:
        alp = Russian_alp
    else:
        alp = English_alp
    nvalue = ""

    for i in value:
        index = alp.find(i)+shift
        if index > alp.index(alp[-1]):
            index = index - alp.index(alp[-1]) - 1

        nvalue += alp[index]
    return nvalue

shifr(value,shift)

def deshifr(value,shift,lang=""):
    symb = value[0]
    if symb in Russian_alp:
        alp = Russian_alp
    else:
        alp = English_alp
    nvalue = ""

    for i in value:
        index = alp.find(i)-shift
        nvalue += alp[index]
    return nvalue

v1 = shifr(value,shift)
print(v1)
v2 = deshifr(v1,shift)
print(v2)







