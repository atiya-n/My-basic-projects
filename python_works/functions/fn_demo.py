
# function with parameter and no return type

def greetings(name):

    print(f"Hello {name}")

greetings("Rocky")

# function with parameter and return type

def add_numbers(num1,num2):

    result = num1 + num2

    return result

add_result = add_numbers(100,200)

print(add_result)


# define a func named odd_even with one parameter [name] and return odd or even.

def odd_even(num):

    return f"{num} is even" if num%2==0 else f"{num} is odd"              #used terniary operator to write the condition in one line

print(odd_even(12))



# create a func last_digit max with 2 parameters num1,num2
# func should return num1 if last digit of num1 is > last digit of num2 else return num2

def last_digit_max(num1,num2):

    return f"{num1} is largest" if num1%10>num2%10 else f"{num2} is largest"

print(last_digit_max(179,872))



# the func can be defined in this type also by already assigning default values in the parameters 
# then there wont be a need to pass the args when calling the func

def smart_div(num1=10,num2=2):

    return num1-num2

print(smart_div())



# create a func exponent with 2 para base,power

def exponent(base,power):

    result = base**power

    return result

print(exponent(3,2))

