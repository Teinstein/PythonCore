# Program to check if the input number is a Armstrong's number or not
# Armstrong's Number is a number whose cubes of individual digits add
# upto the number itself

num = int(input("Enter Number to check if it is Armstrong's :"))
temp = num

sum = 0

while(temp > 0):
    n = temp%10
    temp = int(temp/10)
    sum = sum + pow(n,3)

print("Sum of individual digits is :",sum)

if sum == num:
    print("It is an Armstrong's Number")
else:
    print("It is NOT an Armstrong's Number")
    
