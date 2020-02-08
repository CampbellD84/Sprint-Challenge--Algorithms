#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)

b) O(n ^ 2)

c) O(n)

## Exercise II

building_story = some number
floor = some number
eggs = large amount
broken_eggs = 0
dropped_eggs = 0

def egg_drop(building_story, floor):
for build_floor in range(building_story):
if build_floor >= floor:
eggs -= 1
broken_eggs += 1
else
eggs -= 1
dropped_eggs += 1

    print(f'eggs broken: {broken_eggs}')
    print(f'eggs dropped: {dropped_eggs}')
    print(f'eggs remaining: {eggs}')

Runtime: O(n)
