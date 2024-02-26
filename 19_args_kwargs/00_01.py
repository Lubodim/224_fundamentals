def my_func(param1, param2, *args, **kwargs):
    print(param1)
    print(param2)
    print(args)
    print(kwargs)

my_func(11, 15, "Пепеляшка", "Снежанка", "Спащата красавица", UKTC="Е номер 1", GP4E="Ябълки да яде")

# def my_func(**kwargs):
#     result = ""
#     for k, v in kwargs.items():
#         result += f"{v} {k}\n"
#
#     return result
#
# print(my_func(Spiridon="Hello", Stamat="Bye"))


# def my_func(param1, param2, *args):
#     odd_num = []
#     for el in args:
#         if el % 2 == 1:
#             odd_num.append(el)
#     return odd_num, param2, param1
#
#
# print(my_func(1, 2, 3, 6, 7, 8, 9, 10, 11))

# def my_function(*args):
#     even_num = []
#     for el in args:
#         if el % 2 == 0:
#             even_num.append(el)
#     return even_num
#
#
# print(my_function(1, 2, 34, 11, 18, 22, 7))
