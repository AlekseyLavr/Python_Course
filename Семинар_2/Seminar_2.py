# Задача 1
# n = 123

# res = n // 100 + n // 10 % 10 + n % 10
# print(res)

# Задача 2
# n = 26

# p = int(n // 6)
# k = int((n / 3) * 2)
# s = int(n // 6)
# print(p, k, s)

# Задача 3
# n = "385916"

# n1 = n // 100000
# n2 = n // 10000 % 10
# n3 = n // 1000 % 10
# n4 = n // 100 % 10
# n5 = n // 10 % 10
# n6 = n % 10
# if (n1 + n2 +n3) == (n4 + n5 +n6):
#     print('yes')
# else:
#     print('no')
# if int(n[0]) + int(n[1]) + int(n[2]) == int(n[-1]) + int(n[-2]) + int(n[-3]):
#     print('yes')
# else:
#     print('no')


# # Задача 4
# a = 3
# b = 1
# c = 3

# if c < a * b and (c % a == 0 or c % b == 0):
#     print('yes')
# else:
#     print('no')


# вводится три длины сторон треугольника. определить можно ли из них построить треугольник
# a = 5
# b = 7
# c = 12
# if a + b == c or a + c == b or b + c == a:
#     print('yes')
# else:
#     print('no')

# Задача №9. 
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120
    
# n = int(input())
# fact = 1
# while n > 0:
#     fact *= n
#     n -= 1

# print(fact)











# Задача №11. 
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# a = int(input())
# is_fib = False
# fib_prev = 0 
# fib_next = 1
# n = 2
# while fib_next <= a:

#     if fib_next == a:
#         is_fib = True
#     print(n)
       
#     fib_prev, fib_next = fib_next, fib_prev + fib_next
#     n += 1
# else:
#     print(-1)  

# n = int(input('Введите n: '))
# isFib = False
# fib1 = 0
# fib2 = 1
# fib3 = 1
# nNomer = 0

# while fib1<n:
#     fib1 = fib2
#     fib2 = fib3
#     fib3 = fib1+fib2
#     nNomer += 1
#     if fib1==n:
#         isFib = True
#     print(fib1)

# if isFib:
#     # print(f'φ({nNomer})={n}')
#     print(nNomer)
# else:
#     print(-1)

# Задача №13. 
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# n = 6
# numbers = "-20 30 -40 50 10 -10".split()

# length = 0  # Текущая длина последовательности тёплых дней
# max_length = 0  # Максимальная длина последовательности тёплых дней

# for i in range(n):
#     el = int(numbers[i])

#     if el > 0:
#         length += 1
#     else:
#         length = 0

#     if length > max_length:
#         max_length = length


# print(max_length)

# Задача №15. 
# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9 

# n = 5
# numbers = '5 1 6 5 9'.split()
# print(min(numbers), max(numbers))   

