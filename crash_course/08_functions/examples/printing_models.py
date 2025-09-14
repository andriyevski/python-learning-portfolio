# # This program simulates printing 3D models.
# unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# while unprinted_design:
#     current_design = unprinted_design.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
# print(f"\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

def print_models(unprinted_design, completed_models):
    """
    Imitation print model , when list do not stay empty
    """
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """
    Print information about all printed models
    """
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_design = ['phone case', 'robot pendant', 'dodecahedron','apple case']
completed_models = []

print_models(unprinted_design, completed_models)
show_completed_models(completed_models)
