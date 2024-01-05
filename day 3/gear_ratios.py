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

print(build_matrix(file))