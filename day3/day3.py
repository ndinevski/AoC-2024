import re

with open('day3.txt', 'r') as file:
    text = file.read().strip()   

total = 0
allMuls = re.findall(r'mul\([0-9]+,[0-9]+\)', text)


totalLine = 0
for mul in allMuls:
    mulSplut = mul.split('(')[1].split(')')[0]
    numbers = mulSplut.split(',')
    
    prod = int(numbers[0]) * int(numbers[1])
    print(numbers,prod)
    total += prod

total += totalLine
    

print(total)