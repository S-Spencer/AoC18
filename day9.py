#Import collections to allow use of deque
import collections
"""
Input read to find number of players and the value of the last marble
last_marble is multiplied by 100 for part two of the puzzle
score is set to track the individual scores of each player
game is a deque set up to record the position of each marble It is initialised with the first marble, 0
"""
raw = open("day9_input.txt","r")
data = raw.read()
raw.close()
players = int(data[0:data.find("players")])
last_marble = 100*int(data[data.find("worth")+6:data.find("points")-1])
score = [0]*players
game = collections.deque([0])

"""
Each marble, donated by a number between 1 and last_marble is added to game
If the marble's number is not exactly divisible by 23, game is rotated by 2 spaces and the marble appended
If the marble's number is exactly divisible by 23, the game is rotated by -7 spaces. The previous marble at that point is popped from game.
Its value plus the value of the current marble is added to the score of the current player (found by the remainer of dividing the current marble's value by players)
The answer for part one of the puzzle is found when m is equal to last_marble/100, and the highest score is output
The answer for part two is the highest score once all marbles have been player, and is output 
"""
for m in range(1, last_marble + 1):
    if m % 23 == 0:
        game.rotate(-7)
        score[m % players] += (m + game.pop())
    else:
        game.rotate(2)
        game.append(m)
    if m == last_marble/100:
        print("Part 1 answer: " + str(max(score)))

print("Part 2 answer: " + str(max(score)))
