import sys
from subprocess import call

def cat_file(filename):
    file = open(filename, "r")
    contents = file.read()
    file.close()
    return contents

def main():
    print(cat_file(sys.argv[1]))
    print()
    print(call("cat " + sys.argv[1], shell=True))

if __name__ == '__main__':
    main()