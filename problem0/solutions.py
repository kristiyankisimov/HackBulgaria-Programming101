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

def main():
    print(nth_fibunacci(1))
    print(nth_fibunacci(2))
    print(nth_fibunacci(3))
    print(nth_fibunacci(10))

if __name__ == '__main__':
    main()
