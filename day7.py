import re

lines = []

with open("day7.txt", "r") as input_file:
    lines = input_file.readlines()

def containsThing(s):
    if len(s) < 4:
        return False

    for i in range(0, len(s) - 3):
        if s[i] != s[i + 1] and s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != "*" and s[i + 1] != "*":
            return True

    return False

def arrayContainsThing(a):
    for s in a:
        s = s.replace("[", "").replace("]", "")
        if containsThing(s):
            return True

    return False

def findABAs(a):
    abas = []

    for s in a:
        for i in range(0, len(s) - 2):
            if s[i] == s[i + 2] and s[i] != s[i + 1]:
                abas.append(s[i:i + 3])

    return abas

def makeBABs(a):
    babs = []
    for aba in a:
        babs.append(aba[1] + aba[0] + aba[1])

    return babs

def testString(s):
    supernet = []
    hypernet = re.findall("\[[a-zA-Z]*\]", s)
    for sequence in hypernet:
        supernet.append(s[:s.find(sequence)])
        s = s.replace(supernet[-1], "")
        s = s.replace(sequence, "")

    if len(s) > 0:
        supernet.append(s)

    abas = findABAs(supernet)
    babs = makeBABs(abas)

    for bab in babs:
        for s in hypernet:
            if bab in s:
                return True

    return False

answer = 0

print(testString("aba[bab]xyz"))
print(not testString("xyx[xyx]xyx"))
print(testString("aaa[kek]eke"))
print(testString("zazbz[bzb]cdb"))

for line in lines:
    line = line.strip()
    if line == "":
        continue

    if testString(line):
        answer += 1

print(answer)
