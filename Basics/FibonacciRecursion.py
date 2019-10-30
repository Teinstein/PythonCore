# Program to Print Fibonacci Series using Recursion

# Recursive function to generate Fibonacci series 
def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
noOfTerms = int(input("Enter the number of terms:"))

print("Fibonacci Series:")
for x in range(0,noOfTerms):
    print(fibo(x))