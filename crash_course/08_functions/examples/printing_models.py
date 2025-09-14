# This program simulates printing 3D models.
unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_design:
    current_design = unprinted_design.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
print(f"\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
