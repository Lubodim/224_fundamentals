number = int(input())
my_set = set()
for i in range(number):
    my_set.add(input())
for i in range(len(my_set)):
    print(my_set.pop())


# my_set = {input() for x in range(int(input()))}
# print(my_set)
# for i in range(len(my_set)):
#     print(my_set.pop())

# n = int(input())
# given_names = []
# unique_names = []
# for i in range(n):
#     current_name = input()
#     given_names.append(current_name)
#
# for i in range(len(given_names)):
#     if given_names[i] not in unique_names:
#         unique_names.append(given_names[i])
#
# for i in range(len(unique_names)):
#     print(unique_names[i])