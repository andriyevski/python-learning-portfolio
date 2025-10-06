# Homework from file tasks/9_15_Lottery.md
## Task ## : 9.15
# 9_15_Lottery
from random import randint,sample

seria_numb = (1,2,3,4,5,6,7,8,9,10,"A","B","C","D","E")
random_value = tuple()
my_ticket = (7,8,"D","E")
times = 0


while True:
    random_value = tuple(sample(seria_numb, 4))
    #random_pick = seria_numb[randint(0, len(seria_numb) - 1)]
    times+=1
    #random_value.append(random_pick)
    #if len(random_value) == 4 and my_ticket == tuple(random_value):
    if my_ticket == tuple(random_value):
        print(f"# {times} - Виграшна комбінація: {random_value}")
        break
    #if len(random_value) == 4:
        #print(f"# {times} - Work hard: {random_value}")
        #random_value.clear()
    else:
        print(f"# {times} - Work hard: {random_value}")
