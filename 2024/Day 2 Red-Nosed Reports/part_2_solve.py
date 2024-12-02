from itertools import pairwise

## PLEASE NOTE:
# I got totally stuck with my other solution and wanted to change tactics.

# Read in input text
with open('input_text.txt', 'r') as file:
    reports = [[int(x) for x in line.split()] for line in file]

def safe_report(report):
    steps = [a - b for a, b in pairwise(report)]
    return all(x > 0 and x < 4 for x in steps) or all(x < 0 and x > -4 for x in steps)

def isAnySubsetSafe(report):
    subsets = [report[:i] + report[i+1:] for i in range(len(report))]
    return any(safe_report(subset) for subset in subsets)

part_1 = sum(1 for report in reports if safe_report(report))
part_2 = sum(1 for report in reports if isAnySubsetSafe(report))

print(f"Part 1 Safe Reports: {part_1}") # 230
print(f"Part 2 Safe Reports: {part_2}") # 301

