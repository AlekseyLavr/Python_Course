# Функция - это фрагмент программы используемый многократно.
# Print

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)

# sum_numbers(5)

# # Return
# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sum_numbers(5))

# Можно передавать неограниченное количество аргументов
# def sum_str(*args):
#     res = " "
#     for i in args:
#         res += i
#     return res
# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 'r', 'f'))

# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sum_numbers(5))

# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
# a = sum_numbers(5, 'qwert')
# print(a)

# Модульность

# import modul_1
# # Затем обратиться к модулю
# print(modul_1.max_1(5, 9))

# # Можно указать только функцию
# from modul_1 import max_1
# print(max_1(5, 9))

# Все функции модуля: from ... import *
# Полное название модуля ... сокращенное название модуля ... :      import ... as ...

# Рекурсия - функция, которая вызывает сама себя.
# При описании рекурсии важно указать, КОГДА ФУНКЦИИ НАДО ОСТАНОВИТЬСЯ (БАЗИС РЕКУРСИИ).

# Числа Фибоначчи, через рекурсию:

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# # print(fib(7))

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# Алгоритмы - набор инструкций для выполнения какой-то задачи.

# Быстрая сортировка (принадлежит к стратегии "Разделяй и властвуй")

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     grater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(grater)

# print(quick_sort([14, 5, 9, 6, 3, 58, 7, 2, 7, 5]))

# 1 повторение рекурсии
# array = [10, 5, 2]
# pivot = 10
# less = [5, 2]
# grater = []
# return quick_sort([5, 2]) + [10] + quick_sort([]))

# 2 повторение рекурсии
# array = [5, 2]
# pivot = 5
# less = [2]
# grater = []
# return quick_sort([2]) + [5] + quick_sort([])) # ВАЖНО! не забывать, что здесь помимо вызова рекурсии добавляется список[10]

# 3 повторение рекурсии
# array = [2]
# return [2] # Сработал базовый сценарий

# [2] + [5] + [10] = [2, 5, 10]

# Сортировка слиянием

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left): # Когда закончились все числа справа
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right): # Когда закончились все числа слева
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list_1 = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
# merge_sort(list_1)
# print(list_1)
