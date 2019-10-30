#Program to print factorial of a number

num = input("Enter Number to calc its factorial :")

fact = 1
for i in range(1,int(num) + 1):
    fact = fact * i

print("The Factorial is {0}".format(fact))