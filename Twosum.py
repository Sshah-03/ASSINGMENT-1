def twosum(num, target):
    n = len(num)
    for i in range(n):
        for j in range(i + 1, n):
            if num[i] + num[j] == target:
                return i, j
    return None

num = list(map(int, input("Enter the values (space-separated): ").split()))
target = int(input("Enter the target: "))

result = twosum(num, target)
print("Indexes of the values are: ", result)