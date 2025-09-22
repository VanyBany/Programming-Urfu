from random import choice,randint
#list
# ch = [randint(0,100) for i in range(10)]
# print(ch)
# print(ch.pop(4))
list1 = [[12,3],[234,1],[2345,2]]
print(sorted(list1, key = lambda x: x[1]))

#dict
dicti = {'Виктор': 75,"Джон": 2345, "Дмитрий": 434}
# print(dicti["Виктор"])
# dicti["Володя"] = 5
# print(dicti)
d1 = list(dicti.items())
print(sorted(d1))


#enumerate

# for i, value in enumerate(range(1,11)):
#     print(i,value)