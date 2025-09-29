def print_pack_report(ch):
    if ch % 5 == 0 and ch % 3 == 0:
        print(f"{ch} - расфасуем по 3 или по 5")
    elif ch % 5 == 0:
        print(f"{ch} - расфасуем по 5")
    elif ch % 3 == 0:
        print(f"{ch} - расфасуем по 3")
    else:
        print(f"{ch} - не заказываем!")
ch = int(input("Кол-во пирожных: "))
print_pack_report(ch)