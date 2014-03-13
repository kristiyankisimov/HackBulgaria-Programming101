def check_rows_sum(sudoku):
    return all(map(lambda row: True if sum(row) == 45 else False), sudoku)

def check_cols_sum(sudoku):
    list_cols = []
    for i in range(len(sudoku)):
        list_cols = [row[i] for row in sudoku]
    return all(map(lambda col: True if sum(col) == 45 else False), list_cols)

def check_box_sum(sudoku):
    list_box = []

def get_columns(sudoku):
    list_cols = []
    for i in range(len(sudoku)):
        list_cols = [row[i] for row in sudoku]
    return list_cols