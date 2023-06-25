def evenorodd(number):
    if number % 2 == 0:
        return False
    else:
        return True

number = int(input("enter number:"))
result = evenorodd(number)

if (result == 0):
    print(number,"is true!")
else:
    print(number,"is false!")