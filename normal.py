#Multiplication Table

user_input = int(input("Please input a number of your choice: "))
for i in range(26):
    print(i,"x",user_input, '=', (i * user_input))
    #This line of code not only structures the output but also calculates the answer for me.

#Sentinel-Controlled Iteration
x = 1
count = 0
while count != 1:
    x_input = int(input("Please enter a number of your choice: "))
    if x_input == 0:
        print("x is equal to", x)
        count = 1
    elif x_input % 2 == 0:
        #even options
        if x_input < 0:
            x += x_input
            print(x)
        else:
            x *= x_input
            print(x)
    elif x_input % 2 == 1:
        #odd options
        if x_input < 0:
            x -= x_input
            print(x)
        else:
            x /= x_input
            print(x)
    else:
        print("I don't believe that is an integer, please try again.")
