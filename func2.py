def myfunc(text):
    word = text.split()
    return word[0][0] == word[1][0]
print(myfunc("Suroop Shah"))
print(myfunc("Jay Patel"))