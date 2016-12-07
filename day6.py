lines = []

with open("day6.txt", "r") as input_file:
    lines = input_file.readlines()

positions = [{}, {}, {}, {}, {}, {}, {}, {}]

for line in lines:
    line = line.strip()

    for i in range(0, len(line)):
        pos_dict = positions[i]

        if line[i] in pos_dict:
            pos_dict[line[i]] += 1
        else:
            pos_dict[line[i]] = 1

password = ""
for pos_dict in positions:
    max_value = 99999999
    max_character = "*"

    for k, v in pos_dict.items():
        if v < max_value:
            max_value = v
            max_character = k

    password += max_character

print(password)
