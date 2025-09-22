from string import *
from random import *

def pd():
    letters = "".join(choice(ascii_uppercase) for i in range(3))
    
    chisla = "".join(choice(digits) for i in range(3))

    symbols = "".join(choice(punctuation) for i in range(2))
    
    password =  letters + chisla + symbols

    return password

list_password = list(pd())
shuffle(list_password)

list_password = "".join(list_password)
print(list_password)



