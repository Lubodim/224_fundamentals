from collections import deque
my_queue = deque()

while True:
    command = input()
    if command == "END":
        print(f"{len(my_queue)} people remaining.")
        break
    if command == "PAID":
        while my_queue:
            print(my_queue.popleft())
        continue
    my_queue.append(command)
