# Program to find maximum and minimum from an array

def maxOfArray(arr):
    n = len(arr)
    max = arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max

def minOfArray(arr):
    n = len(arr)
    min = arr[0]
    for i in range(1,n):
        if arr[i] < min:
            min = arr[i]
    return min

n = int(input("Enter no of elements in the array:"))
print("Enter elements of array:")
arr = [ int(input()) for j in range(n) ]

print("Maximum value in array is:",maxOfArray(arr))
print("Minimum value in array is:",minOfArray(arr))
