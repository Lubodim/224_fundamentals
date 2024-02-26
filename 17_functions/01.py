func = lambda x, y: x ** y
a, b = map(int, input().split(", "))

res = func(a, b)
print(f"{a} to the power of {b} = {res}")
