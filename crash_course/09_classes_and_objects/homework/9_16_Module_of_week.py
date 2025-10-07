# Homework from file tasks/9_16_Module_of week.md
## Task ## : 9.16
# 9_16_Module_of week
import time
start = time.monotonic()
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
        total_time = time.monotonic() - start
        print(f"# {times} - Win combination in {total_time:>.2f} seconds : {random_value}")
        break
    #if len(random_value) == 4:
        #print(f"# {times} - Work hard: {random_value}")
        #random_value.clear()
    else:
        print(f"# {times} - Work hard: {random_value}")
