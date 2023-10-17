my_stack = []
num = int(input())
for _ in range(num):
    command = input().split(" ")
    action = 0
    number = 0
    if len(command) > 1:
        action = int(command[0])
        number = int(command[1])
    else:
        action = int(command[0])

    if action == 1:
        my_stack.append(number)
    elif action == 2:
        if my_stack:
            my_stack.pop()
    elif action == 3:
        if my_stack:
            print(max(my_stack))
    elif action == 4:
        if my_stack:
            print(min(my_stack))
    elif action == 5:
        print(len(my_stack))
print(', '.join([str(x) for x in my_stack][::-1]))