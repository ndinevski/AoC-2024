import re

with open('day3.txt', 'r') as file:
    text = file.read().strip()   

r = re.compile("mul\\((\\d+),(\\d+)\\)")
do = re.compile("do\\(\\)")
dont = re.compile("don't\\(\\)")

total = 0

matches = [(m.groups(), m.span()[0]) for m in r.finditer(text)]
dos = [("do", m.span()[0]) for m in do.finditer(text)]
donts = [("dont", m.span()[0]) for m in dont.finditer(text)]

all = matches + dos + donts
all = sorted(all, key=lambda x: x[1])

enabled = True
total = 0

for entry, _ in all:
    if entry == "do":
        enabled = True
    elif entry == "dont":
        enabled = False
    elif enabled:
        total += int(entry[0]) * int(entry[1])

print(total)