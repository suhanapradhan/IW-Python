def is_even_num(l):
    num = []
    for n in l:
        if n % 2 == 0:
            num.append(n)
    return num
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))