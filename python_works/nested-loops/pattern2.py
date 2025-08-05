

# display =>
# 1 2 3 4 5
# 1 2 3 4 
# 1 2 3
# 1 2
# 1

for row in range(1,6):

    for col in range(1,7-row):       #here 7-row= eg: row=1 therefore 7-1st row=6 thus loop travers from 1 to 6 hence prints 12345 and it continues to change dec row and minus from 7 and continue prgm

        print(col,end=" ")

    print()