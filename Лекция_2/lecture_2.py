# Список - это упорядочный конечный набор элементов.
# Создание пустого списка

# list_1 = []
# list_2 = list()

# Вывод списка
# list_1 = [7, 9, 11, 13, 15, 17]
# for i in list_1:
#     print(i, end=' ')
# print()
# print(*list_1) # Звездочка используется для того, чтобы без квадратных скобочек 

# Нумерация списков
# list_1 = [7, 9, 11, 13, 15, 17]
# print(list_1[0])
# print(list_1[-1])
# print(len(list_1)) # Показывает длину списка

# Добавление элементов
# list_1 = [1, 5]
# list_1.append(8)
# print(list_1)
# list_1.append(85)
# print(list_1)

# Добавление элементов с помощью цикла for
# list_1 = []
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# Добавление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# list_1.insert(2, 11)
# print(list_1)

# Удаление последнего элемента из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop())
# a = list_1.pop() # Метод pop удаляет и возвращает удаленное значение
# print(a)

# Удаление кокретного элемента
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0))

# Срезы
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])
# print(list_1[len(list_1) - 1])
# print(list_1[-5])
# print(list_1[:])  # Весь список
# print(list_1[:2]) # От начала (с 0 индекса до 2(не включая 2))
# print(list_1[len(list_1) - 2:]) # До конца
# print(list_1[2:9])
# print(list_1[6:-18])
# print(list_1[0:len(list_1):6]) # 6 - шаг списка
# print(list_1[::6]) # 6 - шаг списка

# Генератор списков (list comprehesion) - это упрощенный подход к созданию списка,
#                   который задействует цикл for, а так же инструкции if-else для 
#                   для определения того, что окажется в финальном списке.

# list_1 = []
# for i in range(1, 101): # последнее число не включается(100 соответствует 101)
#     list_1.append(i)
# print(list_1)

# list_1 = [i for i in range(1, 101)]
# print(list_1)

# Добавим условие(только четные числа):
# list_1 = [i for i in range(1, 101) if i % 2 == 0]
# print(list_1)

# Создадим пары каждому из чисел (кортежи):
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]
# print(list_1)

# Можно *, /, +, -, **
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1)


# Кортеж - неизменяемый список
# Примиряется в случаях защиты каких-либо данных от изменений.

# Создание пустого кортежа
# t = ()
# print(type(t))
# t = (1, ) # запятая в конце обязательна
# print(t)
# print(type(t))
# v = [1, 8 , 9]
# print(type(v))
# print(v)
# v = tuple(v)
# print(type(v))
# print(v)

# # Распаковка кортежа
# a, b, c = v
# print(a, b, c)
# print(type(a))

# Можно добавлять срезы и цикл for
# УДАЛЯТЬ, ПРИБАВЛЯТЬ К КОРТЕЖУ НЕЛЬЗЯ

# t = (1, 2, 3, 5,)
# print(t[1])

# for i in t:
#     print(i)

# for i in range (len(t)):
#     print(t[i])

# Словарь - неупорядочные коллекции произвольных объектов с доступом по ключу.

# Создание пустого словаря
# d = {}
# d = dict()
# print(type(d))

# Добавление значений
# d['q'] = 'qwerty'
# d['w'] = 'werty'
# print(d)
# print(d['q'])

# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓','right':'→'} 
# типы ключей могут отличаться
# print(dictionary['left']) # ←  
# print(dictionary['up']) # ↑ 
# dictionary['left'] = '⇐' 
# print(dictionary['left'])# ⇐ 
# dictionary[585] = 234576
# print(dictionary)
# Если ввести не существующий ключ, то выдаст ошибку
# print(dictionary['type'])# KeyError: 'type'

# удаление элемента 
# del dictionary['left']
# print(dictionary)

# Использoвание циклов for:
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item])) # up: ↑ # down: ↓ # right: → 
# for (k,v) in dictionary.items(): 
#     print('{}: {}'.format(k, v)) # up: ↑ # down: ↓ # right: →

# Множества - содержат в себе уникальные (неповторяющиеся) элементы, не обязательно упорядочные.

# Одно множествоможет содержать значения любых типов. Если у Вас есть два множества, 
# Вы можете совершать над ними любые стандартные операции, например, объединение, пересечение и разность.

# colors = {'red', 'green', 'blue'}
# print(colors)# {'red', 'green', 'blue'} 

# Добавление элементов
# colors.add('red') 
# print(colors) # {'red', 'green', 'blue'} 
# colors.add('gray') 
# print(colors) # {'red', 'green', 'blue','gray'}

# Удаление элементов
# colors.remove('red') 
# print(colors) # {'green', 'blue','gray'} 
# colors.remove('red')# KeyError: 'red' Если удалить уже удаленный элемент, то выскочит ОШИБКА
# colors.discard('red') # ok Пропускает уже удаленный элемент и не выдает ОШИБКУ
# print(colors)# {'green', 'blue','gray'} 

# Удаление всех элементов множества
# colors.clear()# { } 

# Создание пустого множества
# print(colors)# set() 

# Операции со множествами
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}

# Копирование
# c = a.copy()
# print(c)

# Объединение
# u = a.union(b)
# print(u)

# Пересечение
# i = a.intersection(b)
# print(i)

# Разность из a in b
# d_l = a.difference(b)
# print(d_l)

# Разность из b in a
# d_r = b.difference(a)
# print(d_r)
#        2          3           1
# q = a.union(b).difference(a.intersection(b))
# print(q)

# Замороженное множество - неизменяемое множество
# a = {1, 8, 6}
# b = frozenset(a)
# print(b)



