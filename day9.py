lines = []

with open("day9.txt", "r") as input_file:
    lines = input_file.readlines()

def decompress(s):
    decompressed_length = 0
    while len(s) > 0:
        c = s.pop(0).strip()
        if c == "(":
            length = 0
            count = 0

            numStr = ""
            c = s.pop(0)
            while c != "x":
                numStr += c
                c = s.pop(0)

            length = int(numStr)

            numStr = ""
            c = s.pop(0)
            while c != ")":
                numStr += c
                c = s.pop(0)

            count = int(numStr)

            toRepeat = decompress(s[:length])
            s = s[length:]

            decompressed_length += toRepeat * count
        else:
            decompressed_length += len(c)

    return decompressed_length

data = decompress(list(lines[0]))
print(data)
