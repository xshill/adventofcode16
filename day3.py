lines = []

with open("day3.txt", "r") as input_file:
    lines = input_file.readlines()

numbers = []

for line in lines:
    side_str = line.strip().split(" ")
    side_str = [s for s in side_str if s != ""]

    a = int(side_str[0])
    b = int(side_str[1])
    c = int(side_str[2])

    numbers.append(a)
    numbers.append(b)
    numbers.append(c)

no_numbers = len(numbers)
no_valid_triangles = 0

for start_index in range(0, 3):
    i = start_index
    while i < no_numbers:
        a = numbers[i]
        b = numbers[i + 3]
        c = numbers[i + 6]

        if a + b > c and a + c > b and b + c > a:
            no_valid_triangles += 1

        i += 9

print(str(no_valid_triangles) + " of the triangles are possible")
