# Homework from file tasks/8_15_Print_models.md
## Task ## : 8.15
# 8_15_Print_models
import os
import sys

sys.path.append(os.path.abspath('../examples'))


from printing_models import print_models, show_completed_models

unprinted_design = ['phone case', 'robot pendant', 'dodecahedron','apple case']
completed_models = []

print_models(unprinted_design,completed_models)
show_completed_models(completed_models)
