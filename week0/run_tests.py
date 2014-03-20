import os
from subprocess import call

def run_all_tests(filename):
    for root, dirs, files in os.walk("./"):
        for f in files:
            if f == filename:
                call("python3.3 " + root + "/" + f, shell=True)

def main():
    run_all_tests("tests.py")

if __name__ == '__main__':
    main()