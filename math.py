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


courses = ['biology','chemistry','compsci','religion']
for course in courses:
    print(course)




# def sum_of_digits(num):
#     b = 0
#     for n in str(num):
#         b += int(n)
#     return b



