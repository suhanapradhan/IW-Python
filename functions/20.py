num1=[3,5,7,9]
num2=[1,5,8,4]
n=list(filter(lambda x:x in num1, num2))
print("intersection",n)
