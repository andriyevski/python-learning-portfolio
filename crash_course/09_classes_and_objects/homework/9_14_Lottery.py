# Homework from file tasks/9_14_Lottery.md
## Task ## : 9.14
# 9_14_Lottery
from random import randint

seria_numb = (1,2,3,4,5,6,7,8,9,10,"A","B","C","D","E")
random_value = []
numb = 0
alfabet = 0

while len(random_value) < 4:
    random_pick = seria_numb[randint(0, len(seria_numb) - 1)]
    if isinstance(random_pick, int) and numb < 2:
        random_value.append(random_pick)
        numb += 1
    elif isinstance(random_pick, str) and alfabet < 2:
        random_value.append(random_pick)
        alfabet += 1

print(f"Виграшна комбінація: {random_value}")


#or


import random

lottery_pool = [1, 2, 3, 4, 5, "A", "B", "C"]
winning_ticket = random.sample(lottery_pool, 4)
print(winning_ticket)
