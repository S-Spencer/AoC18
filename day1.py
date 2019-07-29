#Input file is stored in a list of commands
commands = []
raw = open("day1_input.txt","r")
for line in raw:
    commands.append(line)
raw.close()

"""
total_c stores the current running sum of the commands
total_h stores a list of all previous (i.e. historic) total_c in order to check for the first time one occurs a second time
end is a variable to keep the loop going until a repeat of total_c occurs
first_pass is set so that the running total can be output after the first full pass of commands in order to answer part one of the task
"""
total_c = 0
total_h = []
end = 0
first_pass = 1

"""
The list of commands is inifitly looped over, where each item is added to total_c
Each time this is checked against total_h
If total_c is in total_h then it has repeated and the code ends, output the current total_c in order to answer part two of the task
Otherwise total_c is added to total_h
"""

while end == 0:
    for command in commands:
        total_c += int(command)
        if total_c in total_h:
            print("Part 2 answer: " + str(total_c))
            end = 1
            break
        else:
            total_h.append(total_c)
#After the first complete pass of the commands list, total_c is output to answer part one of the task
    if first_pass == 1:
        print("Part 1 answer: " + str(total_c))
        first_pass = 0
