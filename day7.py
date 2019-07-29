"""
Read in input into two lists
instructions stores two letters, of which the first step represented by the first letter must be completed befroe the second can be undertaken
"""
instructions = []
alpha = []
raw = open("day7_input.txt","r")
for line in raw:
    part1 = line[5]
    part2 = line[36]
    instructions.append([part1, part2])
raw.close()

"""
Create a list of all possible instructions (ie every letter of the alphabet
Each letter also store a time which corrisponds to how many seconds it takes to complete the task associated with the letter (sec)
This calculated as 60 + (letter's position in alphabet) eg A = 60 + 1
"""
sec = 61
alpha = []
for letter in range(65,91):
    alpha.append([chr(letter),sec])
    sec += 1

#Pass through instructions and make a list (start) of all tasks that can be completed without requiring another task to be finished first
start = []
for letter in alpha:
    check = 0
    for ins in instructions:
        if ins[1] == letter[0]:
            check = 1
    if check == 0:
        start.append([letter[0],letter[1]])

"""
Make a list that for each letter stores all other letters that must be completed before the specified letter can be done (pre_rec)
Skip other any letters that appear in start
"""
pre_rec = []
for letter in alpha:
    if letter in start:
        continue
    temp = [letter[0], letter[1]]
    for line in instructions:
        if line[1] == letter[0]:
            temp.append(line[0])
    pre_rec.append(temp)

#List to store the answer to part 1.
answer1 = []

"""
Populate answer1 with the letters in the order they will be completed
Loop coninues while there are still letters missing from answer1 ie. Number of letters in answer is less than the number of letters in alpha
For each pass of the loop, the list next_step stores all possible actions that could be completed given ones already completed in answer1
First any letters in start that are not in answer1 are added, as they have no pre-requisits
Then any letter not in the answer1 and for which all of its prerequisits are completed are also added
Next step is sorted so that letters are added to answer1 in the correct order
The first item not in answer1 is added to it, and the the loop is started over again
"""
while len(answer1) < len(alpha):
    next_step = []
    for st in start:
        if st[0] not in answer1:
            next_step.append(st[0])
    for pr in pre_rec:
        if pr[0] in answer1:
            continue
        check = 0
        for i in range(2,len(pr)):
            if pr[i] not in answer1:
                check = 1
        if check == 0:
            next_step.append(pr[0])
    next_step.sort()
    for ns in next_step:
        if ns[0] not in answer1:
            answer1.append(ns[0])
            break
#Answer is converted into a string (final) and output
final = "".join(answer1)
print("Part 1 answer: " + final)

"""
answer2 acts as answer1 did but for the send part of the puzzle
workers stores the current state of the 5 workers. Each worker consists of a letter - denoting which task they are working on - and a number which startes how long they have left on the current task
If a work has no letter, the default state is ""
time counts how many complete ticks (times the loop has completed) have occured
started stores a list of tasks which have been started but are not yet complete
"""
answer2 = []
workers = [["",0] for m in range(0,5)]
time = 0
started = []

"""
Again, answer2 is populated with tasks in the order they are completed
Each worker checks for avalible task as was done in part 1 of the puzzle, building a list of next_step
Once next_step is ready, it is checked against started to see if another worker is already working on the task.
If it is free, then the current worker is asigned both that letter and its corresponding time from alpha
Once all workers have checked check to see if a task is avalible, their respective countdown are reduced by one
Each worker is checked to see if the countdown on its current task has reached 0. If so, that task is added to answer2 and the worker is reset to the default state
Finally, the counter tick is increased by 1
Once answer2 has each task stored in it, the loop ends and tick is output
"""
while len(answer2) < len(alpha):
    for worker in workers:
        if worker[1] == 0:
            next_step = []
            for st in start:
                if st[0] not in answer2:
                    next_step.append([st[0],st[1]])
            for pr in pre_rec:
                if pr[0] in answer2:
                    continue
                check = 0
                for i in range(2,len(pr)):
                    if pr[i] not in answer2:
                        check = 1
                if check == 0:
                    next_step.append([pr[0],pr[1]])
            next_step.sort()
            for ns in next_step:
                if ns[0] in started:
                    continue
                if ns[0] not in answer2:
                    worker[0] = ns[0]
                    worker[1] = ns[1]
                    started.append(ns[0])
                    change = 1
                    break
    for worker in workers:
        if worker[1] > 0:
            worker[1] -= 1
    for worker in workers:
        if worker[1] == 0 and worker[0] != "":
            answer2.append(worker[0])
            worker[0] = ""
    time += 1
print("Part 2 answer: " + str(time))
