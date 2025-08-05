# create a func odd_even_count with 1 param [num]
# function display count of odd_num and count of even_num 



def odd_even_count(number):

    even_count = 0

    odd_count = 0

    while(number!=0):

        digit = number%10

        if digit%2==0:

            even_count = even_count+1

        else:

            odd_count = odd_count+1

        number = number//10

    print(f"The even nos in the number are {even_count}")

    print(f"The odd nos in the number are {odd_count}")

odd_even_count(1234)

