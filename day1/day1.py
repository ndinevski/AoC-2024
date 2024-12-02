with open('day2.txt', 'r') as file:
    lines = file.readlines()    
    

safeLines = 0    

for line in lines:
    numbers = line.split()
    safe = True
    
    if len(numbers) < 1:
        continue
    
    if numbers[0] > numbers[1]:
        for i in range(len(numbers)-1):
            if numbers[i] < numbers[i+1]:
                safe = False
    
    if numbers[0] < numbers[1]:
        for i in range(len(numbers-1)):
            if numbers[i] > numbers[i+1]:
                safe = False
                
    if (safe):
        safeLines += 1

print(safeLines)