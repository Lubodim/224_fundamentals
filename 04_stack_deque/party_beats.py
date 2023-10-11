from collections import deque

beats = int(input("Enter a beats in palte: "))
my_deque = deque()


while True:
    command = input()
    if command == "End":
        break
    if command == "Start":
        while True:
            action = input()
            if "refill" in action:
                curren_beats = action.split(" ")[-1]
                beats += int(curren_beats)
                break
            else:
                action = int(action)
                if action <= beats:
                    beats -= action
                    print(f"{my_deque.popleft()} take bites")
                else:
                    pass

    my_deque.append(command)
