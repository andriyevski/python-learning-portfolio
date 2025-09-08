# Homework from file tasks/8_4_Big_T_shirt.md
## Task ## : 8.4
# 8_4_Big_T_shirt
def make_shirt(size: str = "L", text: str = "I love Python") -> None:
    """
    Parameters:
    - size (str): Size of T-shirt -> default = "L"
    - text (str): Text to print standart on T-shirt is 'I love Python'
    return:
    - None
    """
    normalized_size = size.upper()
    valid_size = {"XS", "S", "M", "L", "XL", "XXL"}

    if normalized_size not in valid_size:
        print("Error, you do not pick correct size!")
    else:
        print(f"\nSize of T-shirt: {normalized_size}\nText of T-shirt: {text}")

make_shirt(size="XL",text="Love me PyHard")
make_shirt(size="M")
make_shirt()
