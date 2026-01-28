def myfunc(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)
print(myfunc(2,4))
print(myfunc(3,9))