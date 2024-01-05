sum = 0

file = open("./day 3/part_numbers.txt", "r")

def build_matrix(file):
    matrix = []

    for line in file:
        arr = []

        for char in line:
            if char != "\n":
                arr.append(char)
        
        matrix.append(arr)
    
    return matrix

def check_part_number(row, column, matrix):
    part_numbers= []
    above = row - 1
    below = row + 1
    left = column - 1
    right = column + 1
    
    rows = [above, row, below]
    columns = [left, column, right]

    for i in rows:
        for j in columns:
            if matrix[i][j].isdigit():
                num = build_num(i, j, matrix)
                if num not in part_numbers:
                    part_numbers.append(num)

    return part_numbers

def build_num(row, column, matrix):
    num = [matrix[row][column]]
    temp_column = column

    #check in front
    while matrix[row][temp_column - 1].isdigit():
        temp_column -= 1
        num.insert(matrix[row][temp_column])

    temp_column = column

    #check behind
    while matrix[row][temp_column + 1].isdigit():
        temp_column += 1
        num.append(matrix[row][temp_column])

    return "".join(num)
    


print(build_matrix(file))