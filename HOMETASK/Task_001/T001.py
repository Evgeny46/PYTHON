# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример: *

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print("Введите трехзначное число: ")
a = int(input())  # 123
sum = 0
while a > 0:
    b = a % 10
    sum = sum + b
    a = a // 10
print("Сумма цифр трехзначного числа: ", sum)