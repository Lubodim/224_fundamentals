# my_directory = {}
# print(my_directory)

#
# car_0 = dict(name="John", age=36, country="Norway")
# print(car_0)
# #
#
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(car)
#
#
#
#
#
#
#
#
#
# car_2 = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(car_2)

#
#
# car_3 = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(len(car_3.items()))
#
#
#
# car_4 = {
#   "brand": "Ford",
#   "electric": False,
#   "year": [1964, 2020],
#   "colors": ["red", "white", "blue"]
# }
#
# print(car_4)
# car_4["year"].append(1222)
# car_4["colors"].append("Black")
# print(car_4)
#
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# x = thisdict.get("model")
# x = thisdict.keys()
# y = thisdict.values()
# z = thisdict.items()
# #
# print(x)
# print(y)
# print(z)
#
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
#
#
# print(car) #before the change
# car["color"] = "white",
# print(car) #after the ch
# car["color"] += "Blue",
# print(car) #after the change

#
#
#
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
#
# x = car.values()
# print(x) #before the change
# car["year"] = 2024
# print(x) #after the change
#
#
#
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# x = car.values()
# print(x) #before the change
# car["color"] = "red"
# print(x) #after the change
# x = thisdict.items()
#
#
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.items()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change
#
#
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
#
# x = car.items()
# print(x) #before the change
# car["color"] = "red"
# print(x) #after the change
#
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#     print("Yes, 'model' is one of the keys in the thisdict dictionary")
#
#
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
#
#
#

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "year": 1985
# }
# print(thisdict)
# thisdict.update({"year": 2020})
# print(thisdict)
# thisdict["year"] = 0
# print(thisdict)
#
#
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)
#
#
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})
#
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# x = thisdict.pop("model")
# print(thisdict)
# print(x)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.popitem()
# print(thisdict)
# print(x)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)
#
# for k, v in thisdict.items():
#     print(f"this is value {v}")
#
key_map_dict = {'a': 'apple', 'c': 'cat'}
d = {'a': 1, 'b': 2, 'c': 3}
d = {(key_map_dict[k] if k in key_map_dict else k): v for (k, v) in d.items()}
print(d)




key_map_dict = {'a':'apple','c':'cat'}
d = {'a':1,'b':2,'c':3}
for k, v in d.items():
    if k in key_map_dict:
        d[k] = key_map_dict[k]
print(d)
