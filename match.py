x = int(input("Enter the number: "))
match x:
    case 0:
        print("Value of x is Zero.")
    case _ if x % 2 == 0:
        print("Value of x is divisible by 2.")
    case _ if x % 2 != 0:
        print("Value of x is not divisible by 2.")
    case _:
        print(x)