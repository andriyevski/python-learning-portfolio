# Homework from file tasks/8_3_T_shirt.md
## Task ## : 8.3
# 8_3_T_shirt
def make_shirt(size: str, text: str = "Go Elon Go") -> None:
    """
    Displays the size and text of a T-shirt.
    Parameters:
    - size (str): Size of the T-shirt.
    - text (str): Text to print on the T-shirt. Defaults to 'Go Elon Go'.
    Returns:
    - None
    """
    normalized_size = size.upper()
    if normalized_size not in {"XS", "S", "M", "L", "XL", "XXL"}:
        print("Warning: Unknown size format.")
    else:
        print(f"\nSize of T-shirt: {normalized_size}\nText of T-shirt: {text}")

make_shirt("xl","LOL yeah!")
make_shirt("L")
