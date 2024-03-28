# задача 2
with open("data1.txt", "a") as d:
    while True:
        new_txt = input()
        if new_txt == "end":
            break
        d.write(f"{new_txt}\n")

with open("data1.txt", "r") as d:
    print(d.read())

# import os
# try:
#     os.remove("output.txt")
# except FileNotFoundError:
#     print("output.txt does not exist")
# Задача 1
# with open("output.txt", "a") as write_somthing:
#     write_somthing.write("This is that I want to do!\n")
#
# with open("output.txt", "r") as ws:
#     print(ws.read())
