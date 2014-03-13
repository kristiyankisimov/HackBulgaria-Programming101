def prepare_meal(number):
    n = 0
    for i in range(1, number):
        if number % (3 ** i) == 0:
            n = i
    string = "spam " * n
    string = string[:-1]

    if number % 5 == 0 and string == "":
        string += "eggs"
    elif number % 5 == 0 and string != "":
        string += " and eggs"
    return string