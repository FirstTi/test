teacher_right_hand = 2
teacher_left_hand = 2

ilya_right_hand = 2
ilya_left_hand = 1

a = teacher_right_hand == teacher_left_hand and ilya_left_hand == ilya_right_hand
print(a)
b = teacher_right_hand == teacher_left_hand or ilya_left_hand == ilya_right_hand
print(b)

c = teacher_right_hand == teacher_left_hand or ilya_left_hand == ilya_right_hand and ilya_left_hand > ilya_right_hand
print(c)

d = teacher_right_hand == teacher_left_hand and ilya_left_hand == ilya_right_hand and ilya_left_hand < ilya_right_hand
print(d)

e = not teacher_left_hand > teacher_right_hand
print(e)
