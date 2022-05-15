# Исключения (сообщают об ошибках)
#print(100/0) сама ошибка
try:                          #попытка запустить код в котором подозревается ошибка
    print(int("string"))      # зависимость от расположения ошибки
    print(100/0)

#except ZeroDivisionError:      # обрабатывается только /0, первая ошибка ломает код
#    print("Произошла ошибка")  # выводится сообщение об ошибке, но код продолжает работу
#except ValueError:
#    print("Ошибка перевода строки в число")  # обработка второй ошибки
# except (ZeroDivisionError,ValueError):
#     print("Произошла ошибки 2 шт")

except (ZeroDivisionError,ValueError) as e:
#    print("Произошла ошибки 2 шт")
    print(e)

finally:
    print("Всегда выполняемый код")


a = 1
b = 2
print("Этот код должен всегда отработать")
print(a + b)


