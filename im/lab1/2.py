def getRandom(num):
	square = num ** 2
	print("num=%.4f" % num, end=" ")
	print("square=%.8f" % square)
	s = "0."
	s += str(square)[4:8]
	randomNum = float(s)
	return randomNum


first = 0.2152
for i in range(100):
	print(i + 1)
	first = getRandom(first)