string = input("enter anything consisting of uppercase and lowercase")
def count_case(string):
    x = 0
    y = 0
    for i in string:
        if i.isupper():
            x += 1
        else:
            y += 1
    print('Upper case count: %s' % str(x))
    print('Lower case count: %s' % str(y))
count_case(string)


