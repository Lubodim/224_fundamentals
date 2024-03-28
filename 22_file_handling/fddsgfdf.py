import os
try:
    os.remove("Gosho.txt")
except FileNotFoundError:
    print("Файла не съществува")

# f = open("Gosho.txt", "a")
# f.write("Something\n")
# f.close()
# c = open("Gosho3.txt", "r")
# print(c.read())
# c.close()


# with open("Stamat.txt", "a") as stamo:
#     stamo.write("Hello Stamo!\n")
#     stamo.write("neshto drugo\n")
