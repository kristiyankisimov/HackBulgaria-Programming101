import sys

def count_of_words(words):
    count = 0
    for word in words:
        word_c = list(filter(lambda x: x != '', word.split("\n")))
        count += len(word_c)
    return count

def wc(command, filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    if command == "chars":
        return len(content)
    elif command == "words":
        return count_of_words(content.split(" "))
    elif command == "lines":
        return len(content.split("\n")) - 1

def main():
    print(wc(sys.argv[1], sys.argv[2]))

if __name__ == '__main__':
    main()