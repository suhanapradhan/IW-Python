def insert_string_middle(tag,str):
    return tag[:2]+ str+ tag[2:]
print(insert_string_middle("[[]]", 'Python' ))
print(insert_string_middle('<<>>', 'PHP' ))
