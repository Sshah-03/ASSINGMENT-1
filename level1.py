def myfunc(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "Name is short"
print(myfunc("Macdonald"))
