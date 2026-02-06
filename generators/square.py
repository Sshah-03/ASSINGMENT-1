def square(n):
    for i in range(1, n):
        yield i **2

for j in square(11):
    print(j)

