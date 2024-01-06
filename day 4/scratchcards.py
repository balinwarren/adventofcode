file = open("./day 4/input_scratchcards.txt", "r")

def split_lists(file):
    cards = []

    for line in file:
        line = line.replace("\n", "")
        line = line.split("|")

        line[0] = line[0].split(":")
        del line[0][0]
        line[0] = line[0][0]

        line[0] = line[0].split(" ")
        
        line[1] = line[1].split(" ")
        
        cards.append(line)

    return cards

def count_points(card):
    points = 0

    for num in card[1]:
        if num.isdigit() and num in card[0]:
            if points > 0:
                points *= 2
            else:
                points = 1

    return points

def count_new_scratchers(cards):
    wins = []
    instances = []

    for card in cards:
        win_num = 0

        for num in card[1]:
            if num.isdigit() and num in card[0]:
                win_num += 1

        wins.append(win_num)
        instances.append(1)

    index = 0
    for inst in instances:
        for i in range(inst):   
            for j in range(1, wins[index] + 1):
                instances[index + j] += 1

        index += 1

    sum = 0
    for inst in instances:
        sum += inst

    return sum
    

#part 1 logic
cards = split_lists(file)
sum = 0

for card in cards:
    points = count_points(card)
    sum += points

print(sum)

#part 2 logic
print(count_new_scratchers(cards))