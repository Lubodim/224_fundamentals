func = lambda x,y: x+y
func1 = lambda x,y: x-y
func2 = lambda x,y: x*y
func3 = lambda x,y: x/y

a, b, c = input().split(" ")

if c == "+":
    print(func(int(a), int(b)))
elif c == "-":
    print(func1(int(a), int(b)))
elif c == "*":
    print(func2(int(a), int(b)))
elif c == "/":
    if int(b) == 0:
        print("You can`t divide by ZERO")
    else:
        print(func3(int(a), int(b)))






