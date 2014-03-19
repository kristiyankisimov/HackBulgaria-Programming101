import sys

def concat_files(filenames):
    content = []
    file = open("bumblebee.txt", "a")
    for filename in filenames:
        file_f = open(filename, "r")
        content_f = file_f.read();
        file_f.close()
        content.append(content_f)

    file.write("\n".join(content))
    file.close()

def main():
    concat_files(sys.argv[1::])

if __name__ == '__main__':
    main()