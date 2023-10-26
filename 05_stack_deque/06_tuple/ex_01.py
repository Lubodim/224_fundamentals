numbers = tuple([float(x) for x in input().split(" ")])
my_dict = {}
for digit in numbers:
    if digit not in my_dict:
        my_dict[digit] = 0
    my_dict[digit] += 1

for k, v in my_dict.items():
    print(f"{k} - {v} times")
