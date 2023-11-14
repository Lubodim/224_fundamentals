def unique_names(g):
    unique_set = set()

    for _ in range(g):
        name = input("Въведете име: ")
        unique_set.add(name)

    sorted_names = sorted(unique_set)

    print("Уникалните имена, сортирани в лексикографски ред:")
    for name in sorted_names:
        print(name)


if __name__ == "__main__":
    try:
        N = int(input("Въведете брой имена N: "))
        unique_names(N)
    except ValueError:
        print("Моля, въведете валидно цяло число за броя имена.")