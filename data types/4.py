def frequency(str):
  length = len(str)

  if length > 2:
    if str[-3:] == 'ing':
      str += 'ly'
    else:
      str += 'ing'

  return str
print(frequency('abc'))
print(frequency('string'))
