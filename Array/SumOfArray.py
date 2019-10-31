# Program to calculate sum of all elements in an array

def sumOfArray(arr):
    n = len(arr)
    sum = 0
    for i in range(0,n):
        sum = sum + arr[i]
    return sum
    
n = int(input("Enter no of elements in the array:"))
print("Enter elements of array:")
arr = [ int(input()) for j in range(n) ]

print("Sum of array using our function:",sumOfArray(arr))
print("Sum of array using std function:",sum(arr))    