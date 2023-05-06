def prime(a):
    if a<=1:
        print(a,"is not a prime number")
        
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            print(a,"is not a prime number")
        else:
            print(a,"is a prime number")

        