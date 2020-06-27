s= int(input("enter a number"))
def prime(s):
    if s>1:
        for i in range(2,s):
            if (s%i)==0:
                print("is not a prime number")
                break
            else:
                print(" a prime")
    else:
        print("not a prime number")
prime(s)


