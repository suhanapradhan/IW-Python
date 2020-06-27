list = [{},{},{}]
list1 = [{1,2},{},{}]
print(all(not d for d in list))
print(all(not d for d in list1))