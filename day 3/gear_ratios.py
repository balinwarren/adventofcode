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
    while (temp_column - 1) >= 0:
        if matrix[row][temp_column - 1].isdigit():
            temp_column -= 1
            num.insert(0, matrix[row][temp_column])
        else:
            break

        

    temp_column = column

    #check behind
    while (temp_column + 1) <= (len(matrix[row]) - 1):
        if matrix[row][temp_column + 1].isdigit():
            temp_column += 1
            num.append(matrix[row][temp_column])
        else:
            break

    return "".join(num)
    
#main logic
sum = 0
syms = "@#$%&*=+-/"
matrix = build_matrix(file)
print(matrix)

for row in matrix:
    count = 0
    for column in row:
        row_index = matrix.index(row)
        column_index = count
        if matrix[row_index][column_index] in syms:
            num_list = check_part_number(row_index, column_index, matrix)
            for num in num_list:
                sum += int(num)

        count += 1

print(sum)
