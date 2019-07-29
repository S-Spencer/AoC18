import sys
"""
rindex finds the index for the last instance of a specific item in a list
This is something I borrowed from the internet so cannot claim credit for!
"""
def rindex(lst,item):
    for i, v in enumerate(reversed(lst)):
        if v == item:
            return len(lst) - i - 1
    return None

#growth decides if a pot will contain a plant in the next generation given a string conaining the 2 pots to ether side of the one in question and a list of rules (lst)
def growth(string,lst):
    if string in lst:
        return "#"
    else:
        return "."

"""
Read in the input file
The first line is copied to temp and converted into a list so as to act as the inital state of each pot
grow stores the rules for the specific series of pot required in a generation to make a plant grow in the next
Only rules that cause a plant to grow are stored, as the only other state is an empty pot
"""
raw = open("day12_input.txt","r")
data = []
for line in raw:
    data.append(line.rstrip())
raw.close()

temp = data[0]
pots = [list(temp[15:-1])]
del data[0:2]

grow = []
for line in data:
    if line[9] == "#":
        grow.append(line[0:5])

"""
negative_index stores the number of pots added to the start of the list. Once initialised properly it will be a negative value
This is required as the index of eg pot 0 will increase when pots are added before it in the list
By using negative_index can calculated the number on a pot given its index (pot index + negative_index)
gen is a counter for number of generations
"""
negative_index = 0
gen = 1

"""
It is unreasonable to run this calculation for 50 billion generations!
Instead, presume that after a reasonable number (10000) that plant growth will have entered a set pattern and thus the sum of pot numbers can be modled as y = mx +c (where y it total, and x is number of generations)

Have to add points either end of original input to check for possible changes.
The most . before a # in either direction is 3, eg ...## and ##....
Thus need to check where first and last # occur, and add additional . to accountfor this
This is done using extra_negative and extra_positive, which are lists with enough "." in to place the first or last "#" with enough "." next to it to be significant
negative_index is decreased by the number of "." in extra_negative
past_gen is made by adding extra_negative and extra_poisitive to either side of the previous generation (pots[gen-1])

current_generation stores which pots have plants in using growth
For the two pots at the begining and end of past_gen, extra "." and added
Once all pots in past_gen have been checked, current gen is added to pots

When the 20th generation is reached, the negative index for that generation is stored (negative_index_20) to allow its use later to answer part 1
"""

for gen in range(1,10001):
    extra_negative = []
    extra_positive = []
    if pots[gen-1].index("#") < 3:
        extra_negative = ["."]*(3 - pots[gen-1].index("#"))
        negative_index -= len(extra_negative)
    if rindex(pots[gen-1],"#") > len(pots[gen-1])-4:
        extra_positive = ["."]*(4 - (len(pots[gen-1]) - rindex(pots[gen-1],"#")))
    past_gen = extra_negative + pots[gen-1] + extra_positive

    current_gen = []
    for pot in range(0,len(past_gen)):
        if pot == 0:
            check = "".join([".",".",] + past_gen[0:3])
            current_gen.append(growth(check,grow))
        elif pot == 1:
            check = "".join(["."] + past_gen[0:4])
            current_gen.append(growth(check,grow))
        elif pot == len(past_gen) - 2:
            check = "".join(past_gen[-4:] + ["."])
            current_gen.append(growth(check,grow))
        elif pot == len(past_gen) - 1:
            check = "".join(past_gen[-3:] + [".","."])
            current_gen.append(growth(check,grow))
        else:
            check = "".join(past_gen[pot-2:pot+3])
            current_gen.append(growth(check,grow))
    pots.append(current_gen)
    if gen == 20:
        negative_index_20 = negative_index

"""
gen20 stores the sum of the value of all pots that contain a plant in the 20th generation
Cannot use the y = m*x + c method used for the 50 billion generations as it is unlikely that the growth rate has settled into a pater by generation 20
"""
gen20 = 0
for pot in range(0,len(pots[20])):
    if pots[20][pot] == "#":
        gen20 += (pot + negative_index_20)
print("Part 1 answer: " + str(gen20))

"""
Compare the final 5 generations to see if a pattern has emerged
final_check stores the sum of all planted pot numbers for the final 5 generations
diff then stores the difference between consecutive generations
If these differences are equal, then the multiple m is found. If not, the program is forced to exit
c is found by subtracting m*10000 from the sum of all planted pots in the final generation
The final answer is found by m*50billion + c
"""
final_check = []
for c in range(-5,0):
    genx = 0
    for pot in range(0,len(pots[c])):
        if pots[c][pot] == "#":
            genx += (pot + negative_index)
    final_check.append(genx)
diff = []
for c in range(0,4):
    diff.append(final_check[c+1]-final_check[c])

if diff[0] == diff[1] == diff[2] == diff[3]:
    m = diff[0]
else:
    sys.exit("Convergence not reached! Increase number of generations.")
c = final_check[4] - (m*10000)
gen50b = (m*(5*(10**10))) + c
print("Part 2 answer: " + str(gen50b))
