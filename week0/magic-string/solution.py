def magic_string(string):
    steps = 0
    middle = len(string) // 2
    for i in range(len(string)):
        if i < middle and string[i] == "<":
            steps += 1
        if i >= middle and string[i] == ">":
            steps += 1
    return steps