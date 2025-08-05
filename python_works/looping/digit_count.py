
# set num
# set count as 0
# enter loop
# take last digit
# increment count
# remove the last digit from number 
# last print count 


number = int(input("Enter the number to take count: "))

count = 0

while (number != 0):

    digit = number%10

    count += 1

    number = number // 10

print(count)