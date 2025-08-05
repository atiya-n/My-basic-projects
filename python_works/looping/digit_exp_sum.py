
# question => eg 12 the 1**2 + 2**2 = 5

#  set num
# find digit count
# set sum as 0
# loop
# extract last digit 
# find exponent of last digit
# add the exponent with sum into sum
# remove the last digit
# display sum


number = 12

count = len(str(number))

sum = 0

while(number != 0):

    digit = number % 10
    exponent = digit ** count
    sum = sum + exponent
    number = number //10

print(sum)