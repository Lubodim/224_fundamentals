# def my_func(param1, param2, *args, **kwargs):
#     print(param1)
#     print(param2)
#     print(*args)
#     print(*kwargs)
#
#
# my_func("UKTC", "Is", "Grate", "!", UKTC="uktc", Grate="Great")
#
#
# def missing(*args):
#     return len(args)
#
# print(missing(1, 4, 5))
# print(missing(4, 5, 6, 1, 3))
# print(missing(2, 20, 10, 15, 28, 3, 1))


# def sum_func(*args):
#     result = sum([x for x in args if x % 2 == 0])
#     return result
#
# print(sum_func(1, 4, 5))
# print(sum_func(4, 5, 6, 1, 3))
# print(sum_func(2, 20, 10, 15, 28, 3, 1))



# def class_room(**kwargs):
#     result = ""
#     for key, value in kwargs.items():
#         result += f"{key}\n"
#         for v in value:
#             result += f"{v}\n"
#     return result
#
# print(
#     class_room(
#         Спиридон=[2, 3, 3, 4, 6],
#         Стамат=[6, 6, 6, 2],
#         Анджелина=[3, 3, 4, 3, 5]
#     )
# )
