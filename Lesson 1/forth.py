season = ""
season = input("Введите один из четырех вариантов: Summer, Winter, Autumn, Spring: ")
season = season.lower()
#season = input("Введите время года: ")
if season == "winter":
    print("Оденься теплее")
elif season == "spring" or season == "autumn":
    print("Возьми ветровку")
elif season == "summer":
    print("Одень футболку")
else:
    print("Неверные данные")
