try:
    num = int(input("Input number: "))
    result = 10 / num
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")

print("_" * 50)
