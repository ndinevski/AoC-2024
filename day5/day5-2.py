with open('day5.txt', 'r') as file:
    parts = file.read().split("\n\n")

rules = parts[0].split()
prints = parts[1].split()

total = 0
correctedIndexes = set()

for k in range(len(prints)):
    nums = prints[k].split(",")

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i != j and (nums[j] + '|' + nums[i] in rules):
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                prints[k] = nums
                correctedIndexes.add(k)

for correctedIndex in correctedIndexes:
    line = prints[correctedIndex]

    total += int(line[int(len(line) / 2)])

print(total)