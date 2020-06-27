def notpoor(str):
    notpoor = str.find('not')
    poor = str.find('poor')
    if poor > notpoor and notpoor>0 and poor>0:
        str = str.replace(str[notpoor:(poor+4)], 'good')
        return str
    else:
        return str
print(notpoor('The lyrics is not that poor!'))
print(notpoor('The lyrics is poor!'))

