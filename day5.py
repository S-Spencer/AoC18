"""
Input is stored in string, which is then split into a list (units1) in order to make it easier to process
The final unit is removed as its white space '\n' that shouldnt be included
A copy of units1 is made for part 2 of the task
"""
raw = open("day5_input.txt","r")
for line in raw:
    string = line
raw.close()
units1 = list(string)
del(units1[-1]) #for some reason reading in input file adds a '\n' at the end that should not be there, so this removes it
units2 = units1

"""
Go through the string and delete two adjacent units that are the same letter but different case
place is used as a index of the current position in the string.
finish is used to keep the code iterating over the string until it is complete. It is set to one once place is set to the index of the final character in the string
Each character is checked against the next in the list to see if its the same letter but different case. If so, they are both deleted, and the place index is reduced to check if
removing character creates a new match. Otherwise, place is incremented by one
Then the length of the string is output. It is storred as shortest for use in part 2 of the task
"""
place = 0
finish = 0
while finish == 0:
    if place == len(units1)-1:
        finish = 1
        continue
    if units1[place] != units1[place+1] and units1[place].lower() == units1[place+1].lower():
        del(units1[place+1])
        del(units1[place])
        place -= 1
    else:
        place += 1
shortest = len(units1)
print("Part 1 answer: " + str(shortest))

#A list is created for letters of the alphabet
alpha = []
for letter in range(97,123):
    alpha.append(chr(letter))
"""
Each letter of the alphabet is trialed to see if removing it from the string will result in a shorter result once all pairs are removed again
mock is set up as a temporary copy of the string, from which each letter that matches a specific letter of the alphabet is removed
Then the same process as part one is undertaken on mock. Once complete, the length of mock is recorded if it is shorter than the current shortest string
Once the shortest string is found, its length is output
"""
for letter in alpha:
    finish = 0
    place = 0
    mock = []
    for unit in units2:
        mock.append(unit)
    while finish == 0:
        if place == len(mock):
            finish = 1
            continue
        if mock[place] == letter or mock[place] == letter.upper():
            del(mock[place])
        else:
            place += 1
    finish = 0
    place = 0
    while finish == 0:
        if place == len(mock)-1:
            finish = 1
            continue
        if mock[place] != mock[place+1] and mock[place].lower() == mock[place+1].lower():
            del(mock[place+1])
            del(mock[place])
            place -= 1
        else:
            place += 1
    if len(mock) < shortest:
        shortest = len(mock)
    del(mock)

print("Part 2 answer: " + str(shortest))
