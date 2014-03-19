import sys

def sum_of_numbers(filename):
    file = open(filename, "r")
    content = file.read().split(" ")
    file.close()
    sum_of_numbers_in_file = 0
    if not "" in content:
        sum_of_numbers_in_file = sum(list(map(lambda x: int(x), content)))
    return sum_of_numbers_in_file

def main():
    print(sum_of_numbers(sys.argv[1]))

if __name__ == '__main__':
    main()