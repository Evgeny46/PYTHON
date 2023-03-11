# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
print('Введите граничащее значение: ')
number = 2
list_1 = []
N = int(input())
for i in range(N):
    i = number ** i
    list_1.append(i)
print(list_1)
