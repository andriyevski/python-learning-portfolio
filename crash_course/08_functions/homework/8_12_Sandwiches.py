# Homework from file tasks/8_12_Sandwiches.md
## Task ## : 8.12
# 8_12_Sandwiches
def make_sandwiches(*ingradients):
    """
    Generation sandwiches from ingradient
    - *ingradients -> List of ingradients
    """
    if not ingradients:
        print("\nTake your sandwiches with: ")
        print("- Bread\n- Butter")
    else:
        print("\nTake your sandwiches with: ")
        print("- Bread\n- Butter")
        for ingradient in ingradients:
            print(f"- {ingradient}")


make_sandwiches('cheese','papperoni','tomato','garlic')
make_sandwiches('carrot','cucumbr','tomato','garlic')
make_sandwiches()
