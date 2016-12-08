lines = []

with open("day8.txt", "r") as input_file:
    lines = input_file.readlines()

width = 50
height = 6
ON = "#"
OFF = "."

def printScreen(screen):
    for row in screen:
        print("".join(row))

def drawRect(screen, w, h):
    for i in range(0, h):
        for j in range(0, w):
            screen[i][j] = ON

def shiftList(l, count):
    for i in range(0, count):
        l.insert(0, l.pop())

def shiftRow(screen, index, count):
    shiftList(screen[index], count)

def shiftColumn(screen, index, count):
    column = []
    for i in range(0, height):
        column.append(screen[i][index])

    shiftList(column, count)

    for i in range(0, height):
        screen[i][index] = column[i]

screen = []
for i in range(0, height):
    screen.append([OFF] * width)

for line in lines:
    line = line.strip()
    if line == "":
        continue

    if "rect " in line:
        dimensions = line.replace("rect ", "").split("x")
        drawRect(screen, int(dimensions[0]), int(dimensions[1]))
    elif "rotate row y=" in line:
        params = line.replace("rotate row y=", "").split(" by ")
        shiftRow(screen, int(params[0]), int(params[1]))
    elif "rotate column x=" in line:
        params = line.replace("rotate column x=", "").split(" by ")
        shiftColumn(screen, int(params[0]), int(params[1]))

no_lit = 0
for i in range(0, height):
    for j in range(0, width):
        if screen[i][j] == ON:
            no_lit += 1

printScreen(screen)
print(str(no_lit) + " pixels lit")
