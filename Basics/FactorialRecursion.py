#Program to print factorial of a number using recursion

#recursive function to print factorial
def factorial(n):
    return 1 if(n==0 or n==1) else n * factorial(n-1);

num = int(input("Enter Number to calc its factorial :"))

print("The Factorial of",num ,"is :", factorial(num))
