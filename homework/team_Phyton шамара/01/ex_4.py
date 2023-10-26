total_bites = int(input())
queue = []

while True:
    command = input()

    if command == "Start":
        break
    else:
        queue.append(command)

while True:
    command = input()

    if command == "End":
        break

    if command.startswith("refill"):
        _, beets = command.split()
        total_bites += int(beets)
    else:
        person_name = queue.pop(0)
        bites_requested = int(command)

        if bites_requested <= total_bites:
            print(f"{person_name} take bites")
            total_bites -= bites_requested
        else:
            print(f"{person_name} must wait")

print(f"{total_bites} bites left")