# Homework from file tasks/9_15_Lottery.md
## Task ## : 9.15
# 9_15_Lottery
from random import randint

seria_numb = (1,2,3,4,5,6,7,8,9,10,"A","B","C","D","E")
random_value = []
numb = 0
my_ticket = (7,8,"D","E")
times = 0


while my_ticket != random_value:
    random_pick = seria_numb[randint(0, len(seria_numb) - 1)]
    times+=1
    if my_ticket[numb] == random_pick:
        random_value.append(random_pick)
        numb += 1
    else:
        print(f"# {times} - Work hard: {random_value}")


print(f"# {times} - Виграшна комбінація: {random_value}")
