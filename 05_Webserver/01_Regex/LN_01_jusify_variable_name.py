import re


def main():
	ages = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123"]
	for age in ages:
		ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", age)
		if ret:
			print("\"%s\" matches" % age)
		else:
			print("\"%s\" does not match" % age)


if __name__ == '__main__':
	main()