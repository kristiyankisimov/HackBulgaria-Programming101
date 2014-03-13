def compare(fraction1, fraction2):

    if fraction1[0] * fraction2[1] > fraction2[0] * fraction1[1]:
        return 1
    elif fraction1[0] * fraction2[1] < fraction2[0] * fraction1[1]:
        return -1
    else:
        return 0

def sort_fractions(fractions):
    for i in range(len(fractions) - 1):
        inx = i
        for j in range(i + 1, len(fractions)):
            if compare(fractions[j], fractions[i]) < 0:
                inx = j
        x = fractions[inx]
        fractions[inx] = fractions[i]
        fractions[i] = x
    return fractions