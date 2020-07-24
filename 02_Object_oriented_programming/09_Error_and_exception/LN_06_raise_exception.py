def input_password():
    # 1. Input password
    pwd = input("Password: ")
    # 2. if password >= 8, return password
    if len(pwd) >= 8:
        return pwd
    # 3. else, raise exception
    ex = Exception("The format of password is incorrect")
    raise ex

try:
    print(input_password())
except Exception as result:
    print(result)