# Задача 26: 
# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def f(a, b):
#     if b == 0:
#         return 1
#     return a * f(a, b - 1)

# a = int(input())
# b = int(input())
# print(f(a, b))

# Задача 28: 
# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

# def sum(a, b):
#     if a == 0:
#         return b
#     return sum(a - 1, b + 1)
    
# a = int(input())
# b = int(input())
# print(sum(a, b))

# Решение 2
# def sum(a, b):
#     if a==0 or b==0:
#         return a+b
#     else:
#         return 1 + sum(a,b-1)

# print(sum(5, 4))