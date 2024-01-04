punc = ",:;\n"
sum  = 0

def check_possible(line):
    index = len(line) - 1
    possible = True
    blue = 14
    green = 13
    red = 12

    for color in line[::-1]:
        num = line[index - 1]

        match color:
            case "blue":
                if int(num) > blue:
                    possible = False
            case "green":
                if int(num) > green:
                    possible = False
            case "red":
                if int(num) > red:
                    possible = False
            case _ :
                possible = possible

        index -= 1

    return possible

file = open("./day 2/cube-count.txt", "r")

for line in file:
    for char in line:
        if char in punc:
            line = line.replace(char, "")

    split_line = line.split(" ")
    
    if check_possible(split_line):
        sum += int(split_line[1])
    print(split_line)

print(sum)
