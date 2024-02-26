# lambda функция

# def i(a):
#     return(a)

# print(i(5))

# # ------------

# i_1 = lambda a: a

# print(i_1(5))

# # ------------
# print((lambda a: a)(5))

# -------------

# lst = '1 2 4 8 9'.split()
# print(lst)

# # -------------

# lst_1 = list(map(int, lst))
# print(lst_1)

# # ------------

# lst_2 = list(map(lambda a: a * 2, lst_1))
# print(lst_2)

# # ------------

# lst_3 = list(filter(lambda a: a % 2 == 0, lst_1))
# print(lst_3)

# lst_3 = list(filter(lambda a: a % 2, lst_1))
# print(lst_3)

# lst_3 = list(filter(lambda a: 1, lst_1))
# print(lst_3)

# lst_3 = list(filter(lambda a: 0, lst_1))
# print(lst_3)

# # -------------

# lst_new = [(2, 3), (6, 8), (3, 7)]
# lst_4 = list(filter(lambda a: (a[0] + a[1]) < 10, lst_new))
# print(lst_4)

# # -------------

# lst_6 = list(map(int, input().split()))
# print(lst_6)


# Задача №47. 
# У вас есть код, который вы не можете менять 
# (так часто бывает, когда код в глубине программы используется множество раз
# и вы не хотите ничего сломать): transformation = <???> values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# # или любой другой список transormed_values = list(map(transformation, values)) 
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation. 
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, 
# а нужно получить его как есть. Напишите такое лямбда-выражение transformation, 
# чтобы transformed_values получился копией values. Пример ввода и вывода данных:
# Ввод: 
# values = [1, 23, 42, ‘asdfg’] 
# transformed_values = list(map(trasformation, values)) 
# if values == transformed_values:    
#     print(‘ok’) 
# else:    
#     print(‘fail’) 
# Вывод: 
#       ok

# values = [1, 23, 42, 'asdfg'] 
# transformed_values = list(map(lambda a: a, values)) 
# if values == transformed_values:    
#     print('ok') 
# else:    
#     print('fail')


# Задача №49. 
# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, 
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), 
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. 
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, 
# зато искусственные спутники были были запущены на круговые орбиты. 
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
# При решении задачи используйте списочные выражения. 
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, 
# а затем найти и сам эллипс, имеющий такую  площадь. 
# Гарантируется, что самая далекая планета ровно одна.

# Ввод: 
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
# print(*find_farthest_orbit(orbits)) 
# Вывод: 
# 2.5 10

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# s_orbits = list(filter(lambda a: a[0] != a[1], orbits)) # отфильтровываем круговые орбиты
# s_orbits_1 = max(list(map(lambda a: a[0] * a[1], s_orbits))) # выбираем максимальную орбиту
# find_farthest_orbit = list(filter(lambda a: a[0] * a[1] == s_orbits_1, s_orbits)) # сравниваем с максимальным значением 
# print(*find_farthest_orbit) 

# def find_farthest_orbit(orbits): # создаем функцию
#     s_lict = [(i, i[0] * i[1]) for i in orbits if i[0] != i[1]]
#     # print(s_lict)
#             # используя генератор списков берем полуоси и сразу вычисляем площадь, 
#                                               # и сравниваем, чтобы не было круговых орбит
#     return max(s_lict, key = lambda pair: pair[1])[0]
# # выбирам максимальное значение в паре (i, i[0]*i[1]) по второму элементу(i[0]*i[1]) 
#                                                 # и выводим первый элемент (i)
#     # max_s = max(s_lict, key = lambda pair: pair[1])
#     # print(max_s)
#     # return max_s[0]
# print(*find_farthest_orbit(orbits))

# print(*max(orbits, key = lambda pair: pair[0] * pair[1] * (pair[0] != pair[1])))

# Задача №51. 
# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют 
# одинаковое значение некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику. 
# Ввод: 
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print(‘same’) 
# else: 
#     print(‘different’)
# Вывод: 
#     same


# def same_by(characteristic, objects):
#     a = map(characteristic, objects)
#     b = set(a)
#     if len(b) < 2:
#         return True
#     else:
#         return False
    
# values = [0, 2, 10, 6]     
# if same_by(lambda x: x % 2, values):
#     print('same') 
# else: 
#     print('different')