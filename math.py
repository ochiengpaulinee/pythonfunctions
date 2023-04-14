def add(a,b):
    answer = a+b
    return answer

def subtract(c,d):
    answer = c-d
    return answer

def divide(e,f):
    answer = e/f
    return answer

def multiply(g,h):
    answer = g*h
    return answer

def remainder(i,j):
    answer = i%j
    return answer

    
def sum(*numbers):
    answer = 0
    for number in numbers:
        answer+=number
    return answer

def product(*numbers):
    answer =1
    for number in numbers:
        answer*=number
    return answer
