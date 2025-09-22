from statistics import *

# a = input("Введите строку: ").lower()

# chisla = []
# for i in a:
    
#     if [i,0] not in chisla:
#         chisla.append([i,0])
#     else [i,]
# print(chisla)

symbols = {}
a = input("Введите строку: ").lower()
for i in a:
    if i in symbols.keys():
        symbols[i]+=1
    else:
        symbols[i] = 1

char_list = []
for char, count in symbols.items():
    char_list.append((char,count))
print(char_list)

for i in range(len(char_list)):
    for j in range(i+1,len(char_list)):
        if char_list[i][1] <char_list[j][1]:
            char_list[i], char_list[j] = char_list[j], char_list[i]
print(char_list)

for i in range(3):
    print(char_list[i])




