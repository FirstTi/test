#hint = "Say your name: "
#a = input(hint)

#print(f"Your name is {a}")
DIVISION = 1.8
ABS_ZERO = 32


grad_c = float(input("Введите градусы цельсия: "))   # Пользователь вводит градусы цельсия
grad_f = int(grad_c * DIVISION + ABS_ZERO)
print(f"Температура за окном - {grad_f}")
