


n, m = input().split()
set_1 = set()
set_2 = set()
for i in range(int(n)):
    set_1.add(int(input()))
for i in range(int(m)):
    set_2.add(int(input()))

print(*set_1.intersection(set_2), sep="\n")