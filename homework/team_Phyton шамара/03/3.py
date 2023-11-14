def party_management():
    invited_count = int(input("Въведете брой покани: "))

    invited_guests = set(range(1, invited_count + 1))

    while True:
        command = input("Въведете номер на пристигнала покана или 'End' за край: ")

        if command == "END":
            break

        guest_number = int(command)

        if guest_number in invited_guests:
            invited_guests.remove(guest_number)

    missing_guests = [guest for guest in invited_guests if guest < 10]
    missing_guests += [guest for guest in invited_guests if guest >= 10]

    if missing_guests:
        print(f"Не са дошли {len(missing_guests)} души. Номерата на поканите им са:")
        for guest in missing_guests:
            print(guest)
    else:
        print("Всички покани са били използвани.")


party_management()