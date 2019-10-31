# Program to calculate HCF of two numbers

def hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    
    hcf = 1
    for i in range(1,smaller+1):
        if (x % i) == 0 and (y%i) == 0:
            hcf = i
    return hcf

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print("The HCF of",a,"&",b,"is:",hcf(a,b))