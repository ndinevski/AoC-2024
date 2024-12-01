with open('day1.txt', 'r') as file:
    lines = file.readlines()    
    
leftCol = []
rightCol = []
    
for line in lines:
    numbers = line.split()
    firstNum = int(numbers[0])
    secondNum = int(numbers[1])
    
    leftCol.append(firstNum)
    rightCol.append(secondNum)

leftCol = sorted(leftCol)
rightCol = sorted(rightCol)

sum = 0
    
for i in range(len(leftCol)):
    firstNum = leftCol[i]
    secondNum = rightCol[i]
    
    diff = abs(firstNum - secondNum)
    sum += diff
            
print(sum)