with open('day5.txt', 'r') as file:
    parts = file.read().split("\n\n")

rules = parts[0].split()
prints = parts[1].split()

total = 0

for k in range(len(prints)):
    nums = prints[k].split(",")
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i != j and (nums[j] + '|' + nums[i] in rules):
                prints[k] = "NOPE"
        
for line in prints:
    if line != "NOPE":
        nums = line.split(",")
        total += int(nums[int(len(nums) / 2)])

print(total)