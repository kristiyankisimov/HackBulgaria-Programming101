import sys

def cat2(file_names):
    content = []
    for f in file_names:
        file = open(f, "r")
        c = file.read()
        file.close()
        content.append(c)
    return "\n".join(content)

def main():
    args_list= sys.argv[1::]
    print(cat2(args_list))

if __name__ == '__main__':
    main()
