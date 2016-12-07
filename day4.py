lines = []

with open("day4.txt", "r") as input_file:
    lines = input_file.readlines()

def is_most_common(test_letter, frequency):
    if test_letter not in frequency:
        return False

    test_frequency = frequency[test_letter]

    for letter, count in frequency.items():
        if test_letter != letter:
            if count > test_frequency:
                return False
            elif count == test_frequency and ord(letter) < ord(test_letter):
                return False

    return True

def get_sector_id(line):
    names = line.split("-")
    sector_id = int(names.pop()[:-7])
    checksum = line[-6:-1]

    frequency = {}

    for name in names:
        for letter in name:
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1

    for checksum_letter in checksum:
        if not is_most_common(checksum_letter, frequency):
            return 0

        frequency.pop(checksum_letter)

    return sector_id

for line in lines:
    line = line.strip()

    sector_id = get_sector_id(line)
    if sector_id == 0:
        continue

    name_parts = line.split("-")
    name_parts.pop()
    name = " ".join(name_parts)

    name_decrypted = ""

    shift = sector_id % 26

    for c in name:
        if c == " ":
            name_decrypted += " "
        else:
            name_decrypted += chr((ord(c) - ord("a") + shift) % 26 + ord("a"))

    print(name_decrypted + " " + str(sector_id))
