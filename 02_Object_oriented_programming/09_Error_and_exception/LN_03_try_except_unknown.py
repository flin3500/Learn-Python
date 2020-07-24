try:
    num = int(input("Input number: "))
    result = 10 / num
except ValueError:
    print("ValueError")
except Exception as result:
    print("Error is %s" % result)

print("_" * 50)