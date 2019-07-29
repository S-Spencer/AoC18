"""
n is the length in squares of one edge of the fabric
conflict stores a running total of the number of squares with more than one claim
unique_ID will stroe the ID number of the claim that has no conflicts. There is no claim number 0, so will be clear if none is found
fabric is an n*n grid to represent the fabric. Initially all squares within are 0, but as a claim is made on a square it is incremented by 1
"""
n = 1000
conflict = 0
unique_ID = 0
fabric = [[0]*n for m in range(n)]


"""
Input is read in to make a list of claims
Each line of input is reduced to one with no whitespace (line_nw)
ID is a claims ID number
x and y are the indexes of the top left square of the claim on the fabric
x_len and y_len are the number of squares claimed along each axis
claims stores these values, although x+x_len and y+y_len are stored as we are only interested in the range of x and y values and so only need the maximum
"""

claims = []
raw = open("day3_input.txt","r")
for line in raw:
    line_nw = line.replace(" ","")
    ID = line_nw[line_nw.find("#")+1:line_nw.find("@")]
    x = int(line_nw[line_nw.find("@")+1:line_nw.find(",")])
    y = int(line_nw[line_nw.find(",")+1:line_nw.find(":")])
    x_len = int(line_nw[line_nw.find(":")+1:line_nw.find("x")])
    y_len = int(line_nw[line_nw.find("x")+1:])
    claims.append([ID,x,x+x_len,y,y+y_len])


"""
For each claim, the square of fabric it claims are all increased by +1
The first time an individual square of fabric is claimed by more than one claim (ie when fabric[i][j] == 2, as it has two claims), conflict is incremented by one.
This prevents over counting - only interested in the number of squares with more then one claim, not how many times a conflicted square is claimed
Once all claims are checked, the number of conflicts is output
"""

for claim in claims:
    for i in range(claim[1],claim[2]):
        for j in range(claim[3],claim[4]):
            fabric[i][j] += 1
            if fabric[i][j] == 2:
                conflict += 1
print("Part 1 answer: " + str(conflict))

"""
Now that the fabric is mapped out with claims, it is possible to go back and recheck each claim to see if it is conflicted
unique is set so that it increases if a claim is conflicted at any point. If it remains 0 then unique_ID is set to the ID of the current claim and output
The continue statements are included to reduce computation - once a claim is found to have any conflicts we are no longer interested in it and so should move to the next claim
The break statement is included to finish the loop once the unique ID is found, as the task states there is only one unique ID
"""

for claim in claims:
    unique = 0
    for i in range(claim[1],claim[2]):
        for j in range(claim[3],claim[4]):
            if fabric[i][j] > 1:
                unique += 1
                continue
        if unique > 0:
            continue

    if unique == 0:
        unique_ID = claim[0]
        print("Part 2 answer: " + str(unique_ID))
        break
