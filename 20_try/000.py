def divide(a, b):
    return int(a) / int(b)


while True:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    try:
        print(divide(num1, num2))
    except ZeroDivisionError:
        print("You can not divide by zero")
    except ValueError:
        print("You can not divide by characters")
    else:
        print("successfully divided")
    finally:
        print("That was my calculation")
