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


print(split_lists(file)[10])