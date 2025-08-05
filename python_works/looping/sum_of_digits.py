
# set number
# set sum as 0
# extract last digit
# add lst digit with sum
# remove the last digit from number by floor
# last print the total sum


number = 174

sum = 0

while(number != 0):

    digit = number%10

    sum += digit

    number = number // 10

print(sum)