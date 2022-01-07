# Python pre-work coding questions

# Q-1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    print("Hello" + user_name.upper() + "!")

hello_name('Carlos')

print(hello_name)

# Q-2 Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def odd_numbers():
    numbers = list(range(0, 101))
    for number in numbers:
        if number % 2 !=0:
            print(number)

odd_numbers()

# Q-3 Please write a Python function, max_num_in_list to return the max number of a given list

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([5,1,2,10,18])
print(max_num_in_list([5,1,2,10,18]))

# Q-4 Write a function to return if the given year is a leap year. A leap year is divisible 
# by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')

print(is_leap_year(2022))

# Q-5 Write a function to check to see if all numbers in list are consecutive numbers

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)

print(is_consecutive([1,2,3,4,5]))
print(is_consecutive([1,2,4,5,6]))




