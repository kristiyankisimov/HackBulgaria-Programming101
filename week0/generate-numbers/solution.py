import sys
from random import randint

def create_file(filename, n):
    rand_ints = []
    for i in range(n):
        rand_ints.append(str(randint(1, 1000)))
    file = open(filename, "w")
    file.write(" ".join(rand_ints))
    file.close()

def main():
    create_file(sys.argv[1], int(sys.argv[2]))

if __name__ == '__main__':
    main()