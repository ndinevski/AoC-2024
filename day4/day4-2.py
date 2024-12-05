with open('day4.txt', 'r') as file:
    lines = file.readlines() 

matrix = []

for line in lines:
    matrix.append(list(line.strip()))

count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        current = matrix[i][j]

        # Deleted part 1... it was just bruteforce checking all directions...
        
        if current == "A":
            if i+1 < len(matrix) and j+1 < len(matrix[i]) and i-1 >= 0 and i-1 >= 0:
                if ((matrix[i+1][j+1] == "M" and matrix[i-1][j-1] == "S") or (matrix[i+1][j+1] == "S" and matrix[i-1][j-1] == "M")) \
                    and ((matrix[i+1][j-1] == "M" and matrix[i-1][j+1] == "S") or (matrix[i+1][j-1] == "S" and matrix[i-1][j+1] == "M")):
                        count += 1
        
print(count)
