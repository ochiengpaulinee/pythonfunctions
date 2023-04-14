def my_country(country = "Rwanda"):
    print(f"hello from {country}")



 
# A function named concatenate_args that takes any number of string arguments 
# in positional arguments format and concatenates them into a single string

def concatenate_args(*names):
    single = " "
    for name in names:
        single+=name
    return single


# A function named concatenate_kwargs that takes any number of string arguments
#  in keyword arguments  format and concatenates them into a single string

def concatenate_kwargs(**numbers):
    answer = ""
    for key,value in numbers.items():
        answer+=value
    return answer
