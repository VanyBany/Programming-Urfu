from random import randint

scores = sorted([randint(0,100) for i in range(20)])
print(scores)
print(scores[-1:-4:-1])
student_score = int(input("Баллы Стаса: "))
def check_winners(scores,student_score):
    if student_score in scores[-1:-4:-1]:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей")

check_winners(scores,student_score)

