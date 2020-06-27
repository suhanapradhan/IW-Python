def frequency(str):
  if len(str) < 2: 
    return 'Empty string'

  return str[:2]+ str[-2:]
print(frequency('python'))
