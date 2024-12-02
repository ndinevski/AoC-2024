with open('day2.txt', 'r') as file:
    lines = file.readlines()    

safeLines = 0

def is_safe(numbers):
    if int(numbers[0]) > int(numbers[1]):

        for i in range((len(numbers) - 1)):
            if abs(int(numbers[i]) - int(numbers[i+1])) < 1 or abs(int(numbers[i]) - int(numbers[i+1])) > 3:
                return False
            if int(numbers[i]) < int(numbers[i+1]):
                return False
    else:
        for i in range((len(numbers) - 1)):
            if abs(int(numbers[i]) - int(numbers[i+1])) < 1 or abs(int(numbers[i]) - int(numbers[i+1])) > 3:
                return False
            if int(numbers[i]) > int(numbers[i+1]):
                return False
                
    return True    

for line in lines:
    numbers = line.split()
    origNum = line.split()
    
    if len(numbers) < 1:
        print(line)
        continue
    
    safe = is_safe(numbers)
            
    if (safe):
        safeLines += 1

print(safeLines)
