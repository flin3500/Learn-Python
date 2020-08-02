import re

def main():
	email = input("Input email: ")
	ret = re.match(r"^[a-zA-Z0-9_]{4,20}@[a-zA-Z0-9_]+\.com$", email)
	if ret:
		print("%s matches" % email)
	else:
		print("%s does not match" % email)

if __name__ == '__main__':
	main()