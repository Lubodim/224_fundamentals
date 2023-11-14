# print(*set(input() for _ in range(int(input()))), sep="\n")

n = int(input())
my_set = set()
for _ in range(n):
    name = input()
    my_set.add(name)

print(*my_set, sep="\n")
