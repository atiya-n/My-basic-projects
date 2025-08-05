# create a func named max_odd_number with one param [num]
# it should return largest odd number from num

def max_odd_number(number):

    while(number!=0):

        digit = number%10

        if digit%2!=0:

            print(f"{number} is the largest odd number in the number")

            break

        number = number//10

max_odd_number(2536)