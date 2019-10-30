# Program to print Sum of Squares of first 'n' natural numbers

def sumOfSquares(n):
    sum = 0
    for x in range(1,n+1):
        sum = sum + pow(x,2)
    return sum

n = int(input("Enter value of n for generating sum of sqaures:"))
print("Sum of Squares of first",n ,"numbers is : ", sumOfSquares(n))