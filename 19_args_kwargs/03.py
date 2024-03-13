def class_room(**kwargs):
    result = ""
    for k, value in kwargs.items():
        result += f"{k}\n"
        for v in value:
            result += f"{v}\n"
    return result


print(
    class_room(
        Спиридон=[2, 3, 3, 4, 6],
        Стамат=[6, 6, 6, 2],
        Анджелина=[3, 3, 4, 3, 5]
    )
)
