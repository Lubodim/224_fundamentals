from collections import deque
food_quantity = int(input())
orders = deque(int(x) for x in input().split(" "))

print(max(orders))

while True:
    if orders is None:
        print("Orders complete")
        break
    elif orders is not None:
        a = orders.popleft()
        if a <= food_quantity:
            food_quantity -= a
            continue
        elif a > food_quantity:
            orders.appendleft(a)
            print(F"Orders left: {', '.join(str(r) for r in orders)}")
            break
