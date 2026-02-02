def func():
    while True:
        try:
            n = int(input("Enter a number: "))
        except:
            print("Please, enter a valid number")
            continue
        else:
            break
    print("Your square of entered number is: ",n**2)
func()