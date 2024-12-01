with open('day1.txt', 'r') as file:
    lines = file.readlines()
    
leftCol = []
rightCol = []
    
for line in lines:
    numbers = line.split()
    firstNum = numbers[0]
    secondNum = numbers[1] 
    
    leftCol.append(firstNum)
    rightCol.append(secondNum)

sum = 0

for i in range(len(leftCol)):
    firstNum = int(leftCol[i])
    
    for j in range(len(rightCol)):
        secondNum = int(rightCol[j])
        
        if firstNum == secondNum:
            sum += firstNum

print(sum)