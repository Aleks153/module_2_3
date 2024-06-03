# Решение задачи Нули ничто, отрицание недопустимо!

print('Задача "Нули ничто, отрицание недопустимо!"' '\n'  '\n' 'Решение задачи №1:' '\n')

# Reshenie 1

print('Список чисел, согласно условию задачи: ')
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
a = my_list[index]
while a >= 0:
    if a == 0:
        index = index +1
        a = my_list[index]
        continue
    else:
        print(a)
        index = index + 1
        if index < len(my_list):
            a = my_list[index]
        else:
            break
print('Конец!')

print('__________')

# Reshenie 2

print('Решение задачи №2:' '\n')
print('Список чисел, согласно условию задачи: ')
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
N = len(my_list)
index = 0
while index < N and my_list[index] >= 0:
    if my_list[index] == 0:
        index = index + 1
    else:
        print(my_list[index])
        index = index + 1

print('\n' + 'Конец!')

print('__________')

# Reshenie 3

print('Решение задачи №3:' '\n')
print('Список чисел, согласно условию задачи: ')
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
N = len(my_list)
index = 0
while index < N and my_list[index] >= 0:
        if my_list[index] != 0:
            index = index + 1
        else:
            my_list.remove(my_list[index])
print(my_list[0:index])

print('\n'+'Конец!')

