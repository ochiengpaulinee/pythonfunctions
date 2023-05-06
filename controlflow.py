#Write a function that uses while, if and continue statements 
#to print all the even numbers between 0 and 50. 

def even_numbers():
    x = 0
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x)

#Write a function that takes an integer argument 
#and prints "Prime" if the number is prime, 
#and "Not prime" if the number is not prime.

def prime_number(a):
    if a<=1:
        print("it is not a prime number")
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            print("not prime")
    else:
        print("prime number")



#Write a function that takes a list of integers as input and
# prints the sum of all the even numbers in the list.
def sum_even_numbers(a):
    x = 0
    for i in a:
        if i%2==0:
            x+=i
    return x


#Write a function that takes any two integers as input, 
#and prints the sum of all the numbers between the two integers (inclusive)
# that are divisible by 3.

def total_integers(a,b):
    total = 0
    for i in range(a, b+1):
        if i%3==0:
            total+=i
    print(total)
        
