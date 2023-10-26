food_quantity = int(input())

orders = list(map(int, input().split()))

max_order = max(orders)

used_food = 0
remaining_orders = []

for order in orders:
    if order <= food_quantity - used_food:
        used_food += order
    else:
        remaining_orders.append(order)

print(max_order)

if len(remaining_orders) == 0:
    print("Orders complete")
else:
    print(f"Оставащи поръчки: {', '.join(map(str, remaining_orders))}")