# Program to print all prime numbers in a given range

def isPrime(number):
    noOfFactors = 0
    for i in range(1, number+1):
        if (number%i) == 0:
            noOfFactors+=1
    return True if noOfFactors ==2 else False

lowerLimit = int(input("Enter Lower limit for range:"))
upperLimit = int(input("Enter Upper limit for range:"))

print("Prime nos in range are:")

for j in range(lowerLimit,upperLimit+1):
    if isPrime(j):
        print(" ",j)
