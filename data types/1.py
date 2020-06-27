1.	def frequency(str):
    data = {}
    for n in str:
        keys = data.keys()
        if n in keys:
            data[n] += 1
        else:
            data[n] = 1
    return data
print(frequency('google.com'))
