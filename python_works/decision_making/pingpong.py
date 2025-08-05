
# display
# PINGPONG = num%15
# PING = num%3
# PONG = num%5

num = int(input("Enter the number: "))

if num%15 == 0:

    print("PINGPONG")

elif num%5 == 0:
    
    print("PONG")

elif num%3 == 0:

    print("PING")

