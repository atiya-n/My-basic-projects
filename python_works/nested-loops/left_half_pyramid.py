
# display=>
#           *
#         * *
#       * * *
#     * * * *
#   * * * * *


for row in range(1,6):

    for sp in range(1,7-row):        #to print like this we print space then print the pattern
        
        print(" ",end=" ")

    for col in range(1,row+1):

        print("*",end=" ")

    print()