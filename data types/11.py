def word(str):
    count = dict()
    words = str.split()

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count

print( word('the quick brown fox jumps over the lazy dog.'))

