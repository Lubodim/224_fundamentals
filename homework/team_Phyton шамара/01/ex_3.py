queue = []

while True:
    command = input()

    if command == "PAID":
        while queue:
            print(queue.pop(0))
    elif command == "END":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(command)