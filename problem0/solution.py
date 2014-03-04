def nth_fibonacci(n):
	a = 1
	b = 1
	k = 2
	while k < n:
		k += 1
		c = a
		a = b
		b = c + b
	return b
