list = [1, 2, 3, 4]
string = 'emp'
for i in range(len(list)):
    list[i] = string + str(list[i])
print(list)