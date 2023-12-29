calibration_codes = []
sum = 0

file = open("./day 1/scrambled.txt", "r")

for line in file:
    code = "".join([char for char in line if char.isdigit()])
    new_code = [code[0], code[-1]]
    filtered = "".join(new_code)
    calibration_codes.append(filtered)
    sum += int(filtered)

print(sum)