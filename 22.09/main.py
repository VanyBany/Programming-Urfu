ch = int(input("Введите число: "))
st = ""

if ch > 0: 
    st = "Положительное"
elif ch == 0:
    st = "Ноль"
else: st = "Отрицательное"

print("Чётное" if ch%2==0 else "Нечётное",st,"Принадлежит" if ch in range(10,51) else "Не принадлежит")