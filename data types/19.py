a = ['abc', 'xyz', 'aba', '1221']
count = 0
for element in a:
    if len(element) > 2:
        if element[0] == element[-1:]:
            count += 1
print(count)
