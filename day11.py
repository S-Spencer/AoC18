#Set input serial number as global variable
serial = 8868

"""
power_level returns the power level of a given cell on the grid from its co-ordinates (x,y)
rack stores the rack id of a cell, its x co-ordinate + 10
The power level of the cell (power) is found by multiplying multiplying rack by y, adding the serial then multiplying all by rack again
The digit of the 100ths is then taken, and 5 subtracted from it to give the final value of power
power does the initial multiplications, then is converted into a string in order to more easily identify the hundreths digit (it will always be the character at [-3] in the string)
"""
def power_level(x,y):
    rack = x+10
    power = str(rack*((y*rack)+serial))
    power = int(power[-3])-5
    return power

"""
power_total returns the sum of the power_levels of all cells in a square of dimensions d^2 of whith the top left corner is centred on (x,y)
f is an input list of all fuel cells on the grid
total is the running sum of all power_levels of cells in the square.
All cells in the range (x to x+d, y to y+d) are check for their power level, which is summed and added to the total
This is returned once all cells have been checked
"""
def power_total(x,y,f,d):
    total = 0
    for i in range(x,x+d):
        for j in range(y,y+d):
            total += f[i][j]
    return total

"""
fuel is a list to store the power levels of each individual cell
max_power stores the greatest power found when checking the grid for squares of various size.
maz_power_xyd stores the coordinates of the top left square (x,y) and side length (d) of the square which gives the greates power level
It is initialised as (1,1,300) as the power_level of the full grid will be calculated and stored as the initial max_power whilst fuel is populated
"""
fuel = []
max_power = 0
max_power_xyd = [1,1,300]

"""
populate fuel
For each x value, a list is made (temp) of all power_levels for all possible y values
This is then appended to fuel
"""
for i in range(1,301):
    temp = []
    for j in range(1,301):
        power = power_level(i,j)
        temp.append(power)
        max_power += power
    fuel.append(temp)

#Set an empty list to store the x,y and total power level of the square with the highest power level when a 3 by 3 square is considered (for part 1 of the puzzle)
max_power_3 = [0,0,0]

"""
For every possible square length between 1 to 299 inclusive (300 already calculated fuel was generated), all squares total power level is found
If it beats the previous max power level, the power level is stored in max_power, and the corresponding coordinates and square length are stored in max_power_xyd
An extra check is made for all squares side length of 3 to see which of those has the greatest power level so this can be stored and output for part 1
"""
for d in range(1,300):
    for i in range(0,301-d):
        for j in range(0,301-d):
            square = power_total(i,j,fuel,d)
            if d == 3:
                if square > max_power_3[2]:
                    max_power_3 = [i+1,j+1,square]
            if square > max_power:
                max_power = square
                max_power_xyd = [i+1,j+1,d]
    print(d)
print("Part 1 answer: (" + str(max_power_3[0]) +"," + str(max_power_3[1]) + ")")
print("Part 2 answer: (" + str(max_power_xyd[0]) +"," + str(max_power_xyd[1]) + "), size " + str(max_power_xyd[2]))
