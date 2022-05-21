answer = "8"
attend = 4

while attend != answer:
    attend = input("Введите целое число от 1 до 10: ")
    if attend > answer:
        print("Ты не угадал, ответ меньше")
    elif attend < answer:
        print("Ты не угадал, ответ больше")
    elif attend == answer:
        print("Ты угадал")
        break
    # else:
    #     print("Не верно")
