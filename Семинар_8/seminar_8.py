# Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.

# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

## Решение 1
# dv_ch = list(range(10, 100))
# dv_ch = list(filter(lambda a: a % 9 == 0, dv_ch))
# sun = list(map(lambda a: a * a, dv_ch))
# print(sum(sun))

# # Решение 2
# print(sum(map(lambda x: x * x, filter(lambda x: x % 9 == 0, range(10, 100)))))

# num = '20 -14 88 1 9 -7'

# def check_numbers(str_to_check):
#     num_list = list(filter(lambda x : len(str(abs(int(x)))) ==2, str_to_check.split()))
#     print(*sorted(num_list))

# check_numbers(num)

