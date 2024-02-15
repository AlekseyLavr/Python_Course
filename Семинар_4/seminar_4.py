# Задача N25.
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# input_str = "a a a b c a a d c d d"
# char_count = {}
# result = []

# characters = input_str.split()

# for char in characters:
#     if char in char_count:
#         # char_count[char] += 1
#         print(f"{char}_{char_count[char]}", end=' ')
#     else:
#         # char_count[char] = 0 # a = 0 -> a a = 1
#         print(char, end=' ')
#         #result.append(char)
#     char_count[char] = char_count.get(char, 0) + 1
    #return ' '.join(result)


 # a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2



# Задача N27.
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# row = "She sells sea shells on the sea shore The shells that she sells are sea shells \
#     I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# list_1 = list(row.lower().replace('.', ' ').replace("'", ' ').split())
# print(list_1)
# print(set(list_1))
# print(len(set(list_1)))




# Задача №29. 
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
# n = int(input())
# if max_number > n:
# max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
# n = int(input())
# if max_number < n:
# n = max_number
# print(n)