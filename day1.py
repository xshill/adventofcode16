input_str = "R2, L5, L4, L5, R4, R1, L4, R5, R3, R1, L1, L1, R4, L4, L1, R4, L4, R4, L3, R5, R4, R1, R3, L1, L1, R1, L2, R5, L4, L3, R1, L2, L2, R192, L3, R5, R48, R5, L2, R76, R4, R2, R1, L1, L5, L1, R185, L5, L1, R5, L4, R1, R3, L4, L3, R1, L5, R4, L4, R4, R5, L3, L1, L2, L4, L3, L4, R2, R2, L3, L5, R2, R5, L1, R1, L3, L5, L3, R4, L4, R3, L1, R5, L3, R2, R4, R2, L1, R3, L1, L3, L5, R4, R5, R2, R2, L5, L3, L1, L1, L5, L2, L3, R3, R3, L3, L4, L5, R2, L1, R1, R3, R4, L2, R1, L1, R3, R3, L4, L2, R5, R5, L1, R4, L5, L5, R1, L5, R4, R2, L1, L4, R1, L1, L1, L5, R3, R4, L2, R1, R2, R1, R1, R3, L5, R1, R4"
input_list = input_str.split(", ")

def calculate_distance(location):
    return abs(location[0]) + abs(location[1])

def find_easter_bunny_hq(input_list):
    direction = 90
    current_location = [0, 0]

    locations = [current_location[:]]

    for step in input_list:
        turn = step[0]
        blocks = int(step[1:])

        if turn == "R":
            direction -= 90
        else:
            direction += 90

        direction %= 360

        if direction == 0:
            start = current_location[0] + 1
            end = current_location[0] + blocks + 1

            x = start
            y = current_location[1]

            while x != end:
                location = [x, y]

                print(location)

                if location in locations:
                    return calculate_distance(location)
                else:
                    locations.append(location)

                x += 1

            current_location[0] += blocks
        elif direction == 90:
            start = current_location[1] + 1
            end = current_location[1] + blocks + 1

            x = current_location[0]
            y = start

            while y != end:
                location = [x, y]

                print(location)

                if location in locations:
                    return calculate_distance(location)
                else:
                    locations.append(location)

                y += 1

            current_location[1] += blocks
        elif direction == 180:
            start = current_location[0] - 1
            end = current_location[0] - blocks - 1

            x = start
            y = current_location[1]

            while x != end:
                location = [x, y]

                print(location)

                if location in locations:
                    return calculate_distance(location)
                else:
                    locations.append(location)

                x -= 1

            current_location[0] -= blocks
        else:
            start = current_location[1] - 1
            end = current_location[1] - blocks - 1

            x = current_location[0]
            y = start

            while y != end:
                location = [x, y]

                print(location)

                if location in locations:
                    return calculate_distance(location)
                else:
                    locations.append(location)

                y -= 1

            current_location[1] -= blocks

    return calculate_distance(current_location)

print("Easter Bunny HQ is " + str(find_easter_bunny_hq(input_list)) + " blocks away")
