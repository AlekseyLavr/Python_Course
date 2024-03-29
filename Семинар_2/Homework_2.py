# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. 
# Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, 
# чтобы все монетки лежали одной и той же стороной вверх.

# Входные данные:
# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, 
# если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.

# На входе:
# coins = [0, 1, 0, 1, 1, 0]
# На выходе:
# 3

# coins = [0, 1, 0, 1, 1, 0]
# heads, tails = 0, 0
# for i in coins:
#     if i > 0:
#         heads += 1
#     else:
#         tails += 1
# if heads > tails:
#     print(tails)
# else:
#     print(heads)


# from random import randint
# n = int(input('Введите число монеток: '))
# heads, tails = 0, 0
# for i in range(n):
#     send = randint(0, 1)
#     print(send, end=' ')
#     if send > 0:
#         heads += 1
#     else:
#         tails += 1
# print()
# if heads > tails:
#     print(f'Нужно перевернуть {tails} монет(ы)')
# else:
#     print(f'Нужно перевернуть {heads} монет(ы)')

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. 
# В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.

# Пример
# На входе:
# s = 12
# p = 27
# На выходе:
# 3 9

# s = int(input('Введите сумму двух чисел: '))
# p = int(input('Введите произведение этих же чисел: '))
# for x in range(1, 1001):
#     if x * (s - x) == p and x <= s - x:
#         print(f'Загаданные числа {x} и {s - x}')






# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Пример
# n=16
# Вывод
# 1
# 2
# 4
# 8
# 16

# n = int(input('Введите число N: '))
# k = 0
# res = 1
# while res <= n:
#     print(res, end=" ")
#     k += 1
#     res = 2 ** k