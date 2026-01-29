def up_low(s):
    uppercase = 0
    lowercase = 0
    for i in s:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
        else:
            pass
    return uppercase, lowercase
s = input("Enter a string: ")
upper, lower = up_low(s)
print("Uppercase Count: ",upper)
print("Lowercase Count: ",lower)

