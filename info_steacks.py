stack = [3, 4, 5]
stack.append(8)
stack.append(1)
print(stack) # [3, 4, 5, 8, 1]
pop_element = stack.pop()
print(pop_element)  # 1
print(stack) # [3, 4, 5, 8]
stack.pop()  # 8
stack.pop()  # 5
print(stack) # [3, 4]

