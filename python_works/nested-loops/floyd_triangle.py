
# display=>
# 1
# 2 3
# 4 5 6
# 7 8 9 10

for i in range(1,11):
    
    for row in range(1,5):

        for col in range(1,row+1):

            print(i,end=" ")

        print()