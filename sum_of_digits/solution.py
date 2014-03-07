def sum_of_digits(n):
    sum = 0
    k = abs(n)
    while k != 0:
        sum += k % 10
        k = k // 10
    return sum
def main():
    print(sum_of_digits(1325132435356))
    print(sum_of_digits(123))
    print(sum_of_digits(6))
    print(sum_of_digits(-10))

if __name__ == '__main__':
    main()