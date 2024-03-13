def sum_func(*args):
    even_sum = 0
    for el in args:
        if el % 2 == 0:
            even_sum += el
    return even_sum


print(sum_func(1, 4, 5))
print(sum_func(4, 5, 6, 1, 3))
print(sum_func(2, 20, 10, 15, 28, 3, 1))
