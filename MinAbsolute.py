def minabsolute(arr):
    arr.sort()
    min_diff = float('inf')
    for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i-1])
    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == min_diff:
            result.append([arr[i-1], arr[i]])
    return result
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

output = minabsolute(arr)
print("Output: ",output)