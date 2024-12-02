# Read in input text
with open('input_text.txt', 'r') as file:
    reports = file.read().splitlines()

# Loop over each report
safe_reports = 0
for report in reports:

    # instead of a string of "ints", make a list of ints
    report = [int(x) for x in report.split()]
    
    # set directional and adjacentcy flags and initialize direction
    directional_flag = True
    adjacent_diffs_flag = True
    direction = None

    #Loop over current report by index
    for idx in range(len(report)-1):
        
        # Check difference between current and next value in list
        diff = int(report[idx]) - int(report[idx+1])
        
        # If the diff is not between 1 and 3, change flag and break out of loop
        if not (1<=abs(diff)<=3):
            adjacent_diffs_flag = False
            break

        # First time through loop, assign direction
        if not direction:
            if diff > 0:
                direction = 'up'
            elif diff < 0:
                direction = 'down'

        # If current direction is the same as past direction keep, else set directional flag and break
        if (direction=='up') and (diff > 0):
            direction = 'up'
        elif (direction=='down') and (diff < 0):
            direction = 'down'
        else:
            directional_flag = False
            break

    # If both flags are still true, then add 1 to safe reports
    if directional_flag and adjacent_diffs_flag:
        safe_reports += 1

# return result -- 230
print(f"Safe Reports: {safe_reports}")