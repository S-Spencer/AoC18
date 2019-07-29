import sys

#Generate an alphabet to compare letters to
alpha = []
for letter in range(97,123):
    alpha.append(chr(letter))

#count 2 and count3 respectively store the number of times strings occur containing two or three coppies of the same letter
count2 = 0
count3 = 0

#Read input and store in list of IDs
IDs  = []
raw = open("day2_input.txt","r")
for line in raw:
    IDs.append(line)
raw.close()

"""
For each ID, a comparison is made against the alphabet to see how many times each letter in the alphabet occurs in each indvidual ID
If a letter appears two or three times, this causes count2 or count3 to be incrimented respectively
pass2 and pass3 are used so only the first instance of a dublicate or triplicate letter in an ID is counted (as that is all the task is interested in)
"""
for ID in IDs:
    pass2 = 0
    pass3 = 0
    for letter in alpha:
        n = ID.count(letter)
        if n == 2 and pass2 == 0:
            count2 += 1
            pass2 = 1
        elif n == 3 and pass3 == 0:
            count3 +=1
            pass3 = 1

#Calculate the checksum and output
checksum = count2*count3
print("Part 1 answer: " + str(checksum))

#Find the length of ID
ID_len = len(IDs[0])

"""
Compare one ID (ID1) to another (ID2)
First check the two IDs are not identical, and skip if that is the case
Then check each letter of the same position in both IDs to see if they match
i is the position index for a given letter in the strings
conflict stores the index for a letter if it doesn't match in both IDs.
    As the final answer will only have a single conflict, it does not matter that this would get written multiple times if more than one conglict occurs
matches stores the number of time that the two IDs have identical letters in identical positions
If the number of matches is one less than the number of letters in an ID (ID_len), then two IDs that differ by one letter has been found
ID1 is converted into a list (answer) to allow the removal of the letter at the conflict index, before being converted back to a string for output
"""

for ID1 in IDs:
    for ID2 in IDs:
        if ID1 == ID2:
            continue
        else:
            i = 0
            conflict = 0
            matches = 0
            while i < ID_len:
                if ID1[i] == ID2[i]:
                    matches += 1
                else:
                    conflict = i
                i += 1
            if matches == ID_len - 1:
                answer = list(ID1)
                del answer[conflict]
                answer ="".join(answer)
                sys.exit("Part 2 answer: " + answer)
