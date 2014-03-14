def magic_square(matrix):
    l = []
    d1 = []
    d2 = []
    for i in range(len(matrix)):
        l.append([item[i] for item in matrix])
        d1.append(matrix[i][i])
        d2.append(matrix[i][len(matrix) - i - 1])
    l = [d1] + [d2] + matrix
    s = sum(l[0])
    l = map(lambda x: sum(x), l)
    return all(map(lambda x: True if x == s else False, l))