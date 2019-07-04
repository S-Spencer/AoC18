def step(elf,list):
    move = list[elf] + elf +1
    if move >= len(list):
        move = move%len(list)
        return move
    else:
        return move

recipes = [3,7]
#List to store the scores of each recipe

elfA = 0
elfB = 1
#Values to store the current recipe index of each elf

while len(recipes) < 890701:
    #The new recipie is found by summing the current recepie of each elf
    new_recipe = recipes[elfA] + recipes[elfB]
    #The new recipe is added to the list, including a check to handle if it is double digits.
    if new_recipe > 9:
        recipes.append(1)
        recipes.append(new_recipe%10)
        # The sum of two single digits is less than 20, so the first digit must be "1", and the second will be the remainder when its divided by 10
    else:
        recipes.append(new_recipe)
    #The new index for each elf is then found.
    elfA = step(elfA,recipes)
    elfB = step(elfB,recipes)

answer = 890691
print(recipes[answer:answer+10])
#Print final 10 values of recipes as required by the puzzle
#Its done this way instead of recipe[-10:] as if two recipes are added in the final pass, it throws the final answer off by 1 place.
