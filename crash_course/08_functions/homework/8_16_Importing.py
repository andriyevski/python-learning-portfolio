# Homework from file tasks/8_16_Importing.md
## Task ## : 8.16
# 8_16_Importing
import os, sys

sys.path.append(os.path.abspath('../examples'))

import pizza

pizza.make_pizza(38, 'pepperoni', 'cheeese', 'tomato')

# ------------------------- #

from pets import describe_pet

describe_pet('Gordon')

# ------------------------- #

from greet_users import greet_users as gu

gu('tyson')


# ------------------------- #

import formatted_name as fn

fn.get_formatted_name('Mike', 'Tyson', 'Iron')

# ------------------------- #

from person import *

print(build_person('Oleksandr', 'Usyk', age=37))
