def create(number):
	a, b = 0, 1
	count = 0
	while count < number:
		yield a    #make this become a generator
		a, b = b, a + b
		count += 1


obj = create(50)


while True:
	try:
		ret = next(obj)
		print(ret)
	except Exception as error:
		break
