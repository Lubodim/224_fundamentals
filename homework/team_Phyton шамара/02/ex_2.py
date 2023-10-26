clothes = list(map(int, input().split()))
shelf_capacity = int(input())
shelves_used = 0
current_shelf_load = 0

for cloth in clothes:
    if current_shelf_load + cloth <= shelf_capacity:
        current_shelf_load += cloth
    else:
        shelves_used += 1
        current_shelf_load = cloth

if current_shelf_load > 0:
    shelves_used += 1

print(shelves_used)