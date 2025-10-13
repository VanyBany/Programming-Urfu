from datetime import *
from decimal import Decimal as dec

goods = {}


def add(name, amount, expiration_date, DATE_FORMAT = '%Y-%m-%d'):

    if expiration_date != None:
        expiration_date = datetime.strftime(expiration_date,DATE_FORMAT)
    
    description = {
            "amount": amount,
            "expiration_date": expiration_date
        }
    
    if name in goods:
        goods[name].append(description)

    else:
        goods[name] = list(description)
    
    print(goods)


    



def add_by_note(title,DATE_FORMAT = '%Y-%m-%d'):

    title = title.split(" ")
    name = title[0]
    amount = dec(title[1])
    print(amount)
    expiration_date = title[2]
   

    try:
        expiration_date1 = datetime.strptime(expiration_date,DATE_FORMAT)

    except:
        expiration_date = None

    return add(name,amount,expiration_date)





# def find(title):



# def amount(title):


def menu():

    print("Добро пожаловать в виртуальный холодильник!")
    print("Добавить продукт - 1")
    print("Поиск продуктов по слову - 2")
    print("Кол-во запрошенного продукта - 3")
    print("Выход - 4")

    while True:
        action = input("Введите желаемую операцию(1-3): ").strip()

        if action == "1":
            title = input("Введите название продукта, его кол-во, срок годности(через точку): ")
            add_by_note(title)

        elif action == "2":
             title = input("Введите название продукта: ")
        
        elif action == "3":
            title = input("Введите название продукта: ")

        elif action == "4":
            title = input("До скорых встреч!")
            return

        else:
            print("Введите число от 1 до 3!")
            continue
menu()