# 1. isspace
space = " \r\n\t"
print(space.isspace())

# 2. isalnum
num = "121213213"
print(num.isalnum())

# 3. isalpha
alpha = "adsadsada"
print(alpha.isalpha())


num_str = "1"  # all can be True
# num_str = "⑴" unicode String isdecimal is false
# num_str = "一千" isnumeric can justify chinese number
# 4. isdecimal
print(num_str.isdecimal())
# 5. isdigit
print(num_str.isdigit())
# 6. isnumeric
print(num_str.isnumeric())
