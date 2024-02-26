# Задача 34:  
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке 
# Ввод:   пара-ра-рам рам-пам-папам па-ра-па-дам                                                                                      

# Вывод:  Парам пам-пам

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# phrases = stroka.split()
# if len(phrases) < 2:
#     print('Количество фраз должно быть больше одной!')
# else:
#     count_vowels = []
    
#     for i in phrases:
#         count_vowels.append(len([x for x in i if x.lower() in vowels]))
#     if count_vowels.count(count_vowels[0]) == len(count_vowels):
#         print('Парам пам-пам')
#     else:
#         print('Пам парам')
    




# Задача 36:  
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
# как, например, у операции умножения. 
# Ввод:  print_operation_table(lambda x, y: x * y)                                                                                       
# Вывод:  1         2         3         4           5          6
#         2         4         6         8           10       12
#         3         6         9         12        15       18 
#         4         8         12       16       20       24
#         5        10        15       20       25      30
#         6        12        18       24       30      36


# def print_operation_table(opertion, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         print(' '.join([str(i) for i in range(1, num_columns + 1)]))
#         for i in range(2, num_rows + 1):
#             print(i, end=' ')
#             for j in range(2, num_columns + 1):
#                 print(opertion(i, j), end=' ')
#             print()
# print_operation_table(lambda x, y: x * y, 3, 3)

# def print_operation_table(operation, num_rows, num_columns):
#     result = []
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for i in range(1, num_rows + 1):
#             for j in range(1, num_columns + 1):
#                 if j != num_columns :
#                     result.append(f'{operation(i, j)} ')
#                 else:
#                     result.append(operation(i, j))
#             result.append('\n')
#         print(''.join([str(i) for i in result[:len(result) - 1]]))

# print_operation_table(lambda x, y: x * y, 9, 9)