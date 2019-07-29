"""
find_area finds the size of an area required to contain a group of co-ordinates
It finds the maximum and minimum values for x and y in the input co_ordinates
The area is then found by multiplying the difference in x with the difference in y
"""
def find_area(co_ord):
   x_max = max(co_ord, key=lambda l: l[0])
   x_max = x_max[0]
   x_min = min(co_ord, key=lambda l: l[0])
   x_min = x_min[0]
   y_max = max(co_ord, key=lambda l: l[1])
   y_max = y_max[1]
   y_min = min(co_ord, key=lambda l: l[1])
   y_min = y_min[1]
   area = (x_max - x_min)*(y_max-y_min)
   return area
"""
Input the data for each star and store in lights
x and y store the respecitve coordinates of a light
vx and vy store the veolcities of the lights in the x and y directions
"""
raw = open("day10_input.txt","r")
lights = []
for line in raw:
    x = int(line[10:16])
    y = int(line[18:24])
    vx = int(line[36:38])
    vy = int(line[40:42])
    lights.append([x,y,vx,vy])
raw.close()

"""
area is the size of sky the lights are in
end is a set to keep a loop repeating until alignment occurs
t is the number of ticks that have passed
"""
area = find_area(lights)
end = 0
t = 1

"""
For each pass of the loop, the lights move according to their velocities to a new position
new_pos stores the new position of each light.
For a given loop, this is found by mutliplying vx or vy by t, and adding them to x and y respectively (ie initial position + the number of steps taken*step length)
Once all lights have moved, the new area is found (new_area)
It is assumed the lights will have aligned when they take up the smallest area
If new_area is less than the previous area, it over writes area and the loop repeats
If new_area is greater than area, then the previous loop was the one with the smallest area.
t is reduced by one so it corresponds to the tick which had the smallest area, and is output for the part 2 answer
"""
while end == 0:
    new_pos = []
    for light in lights:
        i = light[0] + t*light[2]
        j = light[1] + t*light[3]
        new_pos.append([i,j])
    new_area = find_area(new_pos)
    if new_area < area:
        area = new_area
    if new_area > area:
        t -= 1
        end = 1
        break
    t += 1
print("Part 2 answer: " + str(t))

"""
align stores the xy co-ordinate of each light at the poitn of alignment
this is found by adding a light's initial xy value to its xy velocity times the number of ticks required to reach alignment
xf_max and yf_max are the final maximum values of x and y respectively
"""
align = []
xf_max = 0
yf_max = 0
for light in lights:
    i = light[0] + t*light[2]
    j = light[1] + t*light[3]
    if i > xf_max:
        xf_max = i
    if j > yf_max:
        yf_max = j
    align.append([i,j])

"""
A blank map of the sky is initialised using xf_max and yf_max. A space without a light in it is denoted by "."
Each light in align is then added into sky. A point when a light is is denoted by "X"
This is then output into a txt file so the aligned lights can be read
"""
sky = [["."]*(xf_max+1) for m in range(yf_max+1)]
for light in align:
    i = light[0]
    j = light[1]
    sky[j][i] = "X"
output = open("Part 1 answer.txt","w+")
for line in sky:
    check = 0
    for element in line:
        if element != ".":
            check = 1
    if check == 1:
        output.write(''.join(line))
output.close()
