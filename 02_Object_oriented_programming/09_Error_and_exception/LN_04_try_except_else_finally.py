try:
    num = int(input("Input number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("ValueError")
except Exception as result:
    print("Error is %s" % result)
else:
    print("Success")
finally:
    print("Always print")

print("_" * 50)