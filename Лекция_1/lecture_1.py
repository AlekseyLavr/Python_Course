# username = input("Ведите имя: ")
# if username == "Маша":
#     print("Ура, это же Маша!")
# elif username == "Петя":
#     print("Привет, Петя.")
# else:
#     print("Hello,", username)

# n = int(input('Введите число: '))
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток от деления числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# Другие методы для работы со строками

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) #
# print('ещё' in text) #
# print(text.lower()) #
# print(text.upper()) #
# print(text.replace('ещё', 'ЕЩЁ'))

# Срезы
# text = 'hello' 
# print(text[:])
# print(text[:2])
# print(text[2:])
# print(text[2:4])
# print(text[::4]) # 4 - шаг текста
