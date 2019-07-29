from operator import itemgetter
import sys

#Read in input to create a map of the tracks
data = []
raw = open("day13_input.txt","r")
for line in raw:
    data.append(line)
raw.close()
tracks = []
for line in data:
    tracks.append(list(line[0:-1]))
"""
x_max and y_max store the mmaximum values of x and y
karts is a list to store each kart. 
It consists of a karts y and x co-ordinate (stored that way due to how the track is stored), the direction it is pointing in, and its next turn direction
The possible directions a kart can face - left, right, up and down - are shown in id_kart
The next turn direction cycle through left (l), centre (c), right (r), then back to l
""" 
x_max = len(tracks[0])
y_max = len(tracks)
karts = []
id_kart =["<",">","^","v"]

"""
Populate karts by reading through tracks
If an element in tracks is in id_kart, then a kart has been found
Its position and direction of facing is store, and its initial turn direction is set to l
The kart is then replace in tracks by the appropriate type of track depending on the direction it was facing
This is done so that each time a kart moves, tracks does not have to be constantly changed
"""
for j in range(0, y_max):
    for i in range(0, x_max):
        if tracks[j][i] in id_kart:
            karts.append([j,i,tracks[j][i],"l"])
            if tracks[j][i] in id_kart[0:2]:
                tracks[j][i] = "-"
            if tracks[j][i] in id_kart[2:]:
                tracks[j][i] = "|"
                
"""
carry_on is set to keep the loop repeating so long as there is more than one kart
crashes is set to allow detection of the first crash for part one of the puzzle
"""                
carry_on = 0  
crashes = 0 

"""
The karts are sorted first by their y co-ordinate, then their x to ensure they are moved in the correct order
crash_IDs is set to store the ID of any kart that crashes (new IDs are set every loop using enumerate)
For each kart:
   A check is made to see if it has already crashed (in case a previous kart in the loop hit it), in which case it can be safely skipped
   The direction the kart is facing is checked, and then compared the track ahead to see what its facing will be after it has moved one step
   Its values in karts are then updated to the new values
   The kart is then check against all other karts, skipping any in crash_IDs or which share an ID (as that would be comparing with itself!)
   If the two karts share x,y co-ordinates they have crashed and are added to crash_IDs.THe position is output the first time a crash occurs to answer part 1 of the puzzle
Once all karts have been checked, kart_update is created. It appends any kart from karts that is not also in crash_IDs. It is then used to update karts
If the length of karts is 1 ie there is only one kart left, it ends the loop and outputs the position of the last kart
"""
while carry_on == 0:
    karts = sorted(sorted(karts, key = itemgetter(1)), key = itemgetter(0))
    crash_IDs = []
    for ID, kart in enumerate(karts):
        if ID in crash_IDs:
            continue
        if kart[2] == ">":
            if tracks[kart[0]][kart[1]+1] == "-":
                kart = [kart[0],kart[1]+1,">",kart[3]]
            elif tracks[kart[0]][kart[1]+1] == "/":
                kart = [kart[0],kart[1]+1,"^",kart[3]]
            elif tracks[kart[0]][kart[1]+1] == "\\":
                kart = [kart[0],kart[1]+1,"v",kart[3]]
            elif tracks[kart[0]][kart[1]+1] == "+":
                if kart[3] == "l":
                    kart = [kart[0],kart[1]+1,"^","c"]
                elif kart[3] =="c":
                    kart = [kart[0],kart[1]+1,">","r"]
                elif kart[3] == "r":
                    kart = [kart[0],kart[1]+1,"v","l"]
            else:
                sys.exit("ERROR: Off the rails!")
        elif kart[2] == "<":
            if tracks[kart[0]][kart[1]-1] == "-":
                kart = [kart[0],kart[1]-1,"<",kart[3]]
            elif tracks[kart[0]][kart[1]-1] == "/":
                kart = [kart[0],kart[1]-1,"v",kart[3]]
            elif tracks[kart[0]][kart[1]-1] == "\\":
                kart = [kart[0],kart[1]-1,"^",kart[3]]
            elif tracks[kart[0]][kart[1]-1] == "+":
                if kart[3] == "l":
                    kart = [kart[0],kart[1]-1,"v","c"]
                elif kart[3] =="c":
                    kart = [kart[0],kart[1]-1,"<","r"]
                elif kart[3] == "r":
                    kart = [kart[0],kart[1]-1,"^","l"]
            else:
                sys.exit("ERROR: Off the rails!") 
        elif kart[2] == "^":
            if tracks[kart[0]-1][kart[1]] == "|":
                kart = [kart[0]-1,kart[1],"^",kart[3]]
            elif tracks[kart[0]-1][kart[1]] == "/":
                kart = [kart[0]-1,kart[1],">",kart[3]]
            elif tracks[kart[0]-1][kart[1]] == "\\":
                kart = [kart[0]-1,kart[1],"<",kart[3]]
            elif tracks[kart[0]-1][kart[1]] == "+":
                if kart[3] == "l":
                    kart = [kart[0]-1,kart[1],"<","c"]
                elif kart[3] =="c":
                    kart = [kart[0]-1,kart[1],"^","r"]
                elif kart[3] == "r":
                    kart = [kart[0]-1,kart[1],">","l"]
            else:
                sys.exit("ERROR: Off the rails!")
        elif kart[2] == "v":
            if tracks[kart[0]+1][kart[1]] == "|":
                kart = [kart[0]+1,kart[1],"v",kart[3]]
            elif tracks[kart[0]+1][kart[1]] == "/":
                kart = [kart[0]+1,kart[1],"<",kart[3]]
            elif tracks[kart[0]+1][kart[1]] == "\\":
                kart = [kart[0]+1,kart[1],">",kart[3]]
            elif tracks[kart[0]+1][kart[1]] == "+":
                if kart[3] == "l":
                    kart = [kart[0]+1,kart[1],">","c"]
                elif kart[3] =="c":
                    kart = [kart[0]+1,kart[1],"v","r"]
                elif kart[3] == "r":
                    kart = [kart[0]+1,kart[1],"<","l"]
            else:
                sys.exit("ERROR: Off the rails!")
        karts[ID] = kart
        for other_ID, other_kart in enumerate(karts):
            if other_ID in crash_IDs or ID == other_ID:
                continue
            else:
                if kart[0:2] == other_kart[0:2]:
                    crash_IDs.append(ID)
                    crash_IDs.append(other_ID)
                    if crashes == 0:
                        print("Part 1 answer: (" + str(kart[1]) + "," + str(kart[0]) + ")")
                        crashes = 1
    karts_update = []
    for update_ID, update_kart in enumerate(karts):
        if update_ID in crash_IDs:
            continue
        else:
            karts_update.append(update_kart)
    karts = karts_update
    if len(karts) == 1:
        carry_on = 1

print("Part 2 answer: (" + str(karts[0][1]) + "," + str(karts[0][0]) + ")") 
   
