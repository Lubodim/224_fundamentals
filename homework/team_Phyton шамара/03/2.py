def parking_management():
    n = int(input("Въведете брой събития: "))

    parking_lot = set()

    for _ in range(n):
        event = input("Въведете събитие (вход/изход, номер на кола): ")
        action, car_number = event.split(', ')

        if action == "in":
            parking_lot.add(car_number)
        elif action == "out" and car_number in parking_lot:
            parking_lot.remove(car_number)

    if parking_lot:
        print("Автомобилите в паркинга са:")
        for car in parking_lot:
            print(car)
    else:
        print("Parking is Empty")


if __name__ == "__main__":
    parking_management()