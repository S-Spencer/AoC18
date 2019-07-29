"""
Input is stored in data, then converted into useable form stored in list of co-ordinates (co_ord)
Each individual co_ord stores the x and y co-ordinate for the point, an ID value, and the value for the number of spaces for which this point is the nearest (initially set to 0)
THe maximum values of x and y are also stored so that a grid of the area of interest can be made (danger)
For each square in danger, the ID of the closest point stored in co_ord will eventually be written, so it is initiated with all squares set to 0 (lowest ID number is 1)
"""
raw = open("day6_input.txt","r")
data = []
for line in raw:
    data.append(line)
raw.close()

co_ord = []
ID = 1
x_max = 0
y_max = 0
for line in data:
    x = int(line[:line.find(",")])
    y = int(line[line.find(",")+1:])
    if x > x_max:
        x_max = x
    if y > y_max:
        y_max = y
    co_ord.append([x,y,ID,0])
    ID +=1
danger = [[0]*(x_max+1) for m in range(y_max+1)]

"""
Each square in danger is asigned the ID of the space in co_ord to which it has the lowest manhattan distance.
If a given square has a a manhattan distance of equal value to two different spaces in co_ord, it is set to -1 as it is a conflicted square
manhattan distance is found by summing the absolute difference of both the x and y co-ordinates of two spaces
"""
i = 0
while i <= x_max:
    j = 0
    while j <= y_max:
        min_distance = x_max + y_max
        min_ID = 0
        for co in co_ord:
            manhattan = abs(i - co[0]) + abs(j- co[1])
            if manhattan == min_distance:
                min_ID = -1
            if manhattan < min_distance:
                min_distance = manhattan
                min_ID = co[2]
        danger[i][j] = min_ID
        j += 1
    i += 1

"""
Make a list of ID values which would end up having infinite area as they touch the edge of the map
For each square on the border of the danger area, its ID value is added to the infinites list if it is not already present
"""
infinites = []
j = 0
while j <= y_max:
    if danger[0][j] not in infinites and danger[0][j] > 0:
        infinites.append(danger[0][j])
    if danger[x_max][j] not in infinites and danger[x_max][j] > 0:
        infinites.append(danger[x_max][j])
    j += 1
i = 0
while i <= x_max:
    if danger[i][0] not in infinites and danger[i][0] > 0:
        infinites.append(danger[i][0])
    if danger[i][y_max] not in infinites and danger[i][y_max] > 0:
        infinites.append(danger[i][y_max])
    i += 1

"""
For every square in danger, find the corrisponding item in co_ord by its ID and increase the value of the number of spaces associated with it (co_ord[index of a given space][3])
This is skipped if the item in co_ord would have infinite area
co_ord_index is calculated as the ID number is one more than the list index in co_ord
"""
for x in range(0,x_max):
    for y in range(0,y_max):
        if danger[x][y] not in infinites:
            co_ord_index = danger[x][y] - 1
            co_ord[co_ord_index][3] += 1
#Find the space in co_ord which claims the greatest area and output
area_max = 0
for co in co_ord:
    if co[3] > area_max:
        area_max = line[3]
print("Part 1 answer: " + str(area_max))

"""
A safe space is defined as any space where the sum of the manhattan distance to all items in co_ord is less than 10000, and the safe area is the sum of the number of safe spaces
For each space in the area previously defined, the manhattan is calculated to each space in co_ord and summed
This is then checked against the value 10000, and if it is less the value of safe_area is incremented by one
Once all spaces have been checked, the value of the safe area is output
"""
safe_area = 0
for i in range(0,x_max):
    for j in range(0,y_max):
        manhattan = 0
        for co in co_ord:
            manhattan += (abs(i-co[0])+abs(j-co[1]))
        if manhattan < 10000:
            safe_area += 1
print("Part 2 answer: " + str(safe_area))
