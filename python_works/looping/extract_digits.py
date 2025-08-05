
number = 274

# loop number != 0
# step1: extract last_digit => last_digit = number%10
# step2: floor => number = number // 10

while(number != 0):

    last_digit = number%10

    print(last_digit)

    number = number // 10