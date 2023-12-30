num_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

calibration_codes = []
sum = 0

def forward(line):
    temp_line = []
    for char in line:
        if char.isdigit():
            return char
        temp_line.append(char)
        temp_line = ["".join(temp_line)]
        for key in num_dict:
            if key in temp_line[0]:
                return num_dict[key]
            
def backward(line):
    temp_line = []
    for char in line[::-1]:
        if char.isdigit():
            return char
        temp_line.insert(0, char)
        temp_line = ["".join(temp_line)]
        for key in num_dict:
            if key in temp_line[0]:
                return num_dict[key]
            
file = open("./day 1/scrambled.txt", "r")

for line in file:
    code = [forward(line), backward(line)]
    filtered = "".join(code)

    calibration_codes.append(filtered)
    sum += int(filtered)

print(calibration_codes)
print(sum)