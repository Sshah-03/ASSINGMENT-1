import random

def high_low(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for j in high_low(1, 10, 12):
    print(j)
